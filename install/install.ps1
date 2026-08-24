param(
  [switch]$Full,
  [switch]$SupportOnly,
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"

if ($Full -and $SupportOnly) {
  throw "Choose either -Full or -SupportOnly, not both. Full mode is the default for installs and updates."
}

$Mode = "full"
if ($SupportOnly) { $Mode = "support-only" }
if ($Full) { $Mode = "full" }

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..")
$CodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$LegacyUserSkillsHome = if ($env:USER_SKILLS_HOME) { $env:USER_SKILLS_HOME } else { Join-Path $HOME ".agents\skills" }
$Timestamp = Get-Date -Format "yyyyMMddHHmmss"
$ManifestPath = Join-Path $CodexHome ".coding-agent-playbook-codex-managed-files.tsv"
$LegacyManifestPath = Join-Path $CodexHome ".codex-agent-playbook-managed-files.tsv"

function Write-Step($Message) {
  Write-Host $Message
}

function Invoke-InstallCommand {
  param([scriptblock]$Command, [string]$Display)
  if ($DryRun) {
    Write-Host "[dry-run] $Display"
  } else {
    & $Command
  }
}

function Get-FileSha256 {
  param([string]$Path)
  return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
}

function Backup-File {
  param([string]$Path)
  if (Test-Path -LiteralPath $Path -PathType Leaf) {
    $Backup = "$Path.bak.$Timestamp"
    Write-Step "Backing up $Path -> $Backup"
    Invoke-InstallCommand { Copy-Item -LiteralPath $Path -Destination $Backup -Force } "Copy-Item '$Path' '$Backup'"
  }
}

function Copy-PlaybookFile {
  param([string]$Source, [string]$Destination)
  $Parent = Split-Path -Parent $Destination
  Invoke-InstallCommand { New-Item -ItemType Directory -Force -Path $Parent | Out-Null } "New-Item -ItemType Directory -Force '$Parent'"
  if (Test-Path -LiteralPath $Destination -PathType Leaf) {
    if ((Get-FileSha256 $Source) -eq (Get-FileSha256 $Destination)) {
      Write-Step "Unchanged $Destination"
      return
    }
  }

  Backup-File $Destination
  Write-Step "Installing $Destination"
  Invoke-InstallCommand { Copy-Item -LiteralPath $Source -Destination $Destination -Force } "Copy-Item '$Source' '$Destination'"
}

function Copy-PlaybookTree {
  param([string]$SourceDir, [string]$DestinationDir)
  if (-not (Test-Path -LiteralPath $SourceDir -PathType Container)) {
    Write-Step "Skipping missing source directory: $SourceDir"
    return
  }

  Get-ChildItem -LiteralPath $SourceDir -Recurse -File | ForEach-Object {
    $RelativePath = $_.FullName.Substring((Resolve-Path $SourceDir).Path.Length).TrimStart('\','/')
    $Dest = Join-Path $DestinationDir $RelativePath
    Copy-PlaybookFile $_.FullName $Dest
  }
}

function Assert-SafeManifestRelativePath {
  param([string]$RelativePath)

  if ([string]::IsNullOrWhiteSpace($RelativePath) -or
      [System.IO.Path]::IsPathRooted($RelativePath) -or
      $RelativePath.Contains("`t") -or
      $RelativePath.Contains("`r") -or
      $RelativePath.Contains("`n")) {
    throw "Unsafe managed-file manifest path: '$RelativePath'"
  }

  $Segments = $RelativePath -split '[/\\]'
  if ($Segments | Where-Object { $_ -in @('', '.', '..') }) {
    throw "Unsafe managed-file manifest path: '$RelativePath'"
  }
}

function Get-ManagedDestination {
  param([System.Collections.IDictionary]$ManagedRoots, [string]$RootName, [string]$RelativePath)

  if (-not $ManagedRoots.Contains($RootName)) {
    throw "Unknown managed-file root '$RootName'."
  }

  Assert-SafeManifestRelativePath $RelativePath
  $DestinationRoot = [System.IO.Path]::GetFullPath($ManagedRoots[$RootName].Destination)
  $NativeRelativePath = $RelativePath -replace '/', [System.IO.Path]::DirectorySeparatorChar
  $Destination = [System.IO.Path]::GetFullPath((Join-Path $DestinationRoot $NativeRelativePath))
  $RootPrefix = $DestinationRoot.TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar

  if (-not $Destination.StartsWith($RootPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Managed-file destination escapes '$DestinationRoot': '$RelativePath'"
  }

  return $Destination
}

function Get-CurrentManifestEntries {
  param([System.Collections.IDictionary]$ManagedRoots)

  $Entries = @()
  foreach ($RootName in $ManagedRoots.Keys) {
    $SourceRoot = (Resolve-Path -LiteralPath $ManagedRoots[$RootName].Source).Path
    foreach ($File in Get-ChildItem -LiteralPath $SourceRoot -Recurse -File) {
      $RelativePath = $File.FullName.Substring($SourceRoot.Length).TrimStart('\', '/') -replace '\\', '/'
      Assert-SafeManifestRelativePath $RelativePath
      $Entries += [pscustomobject]@{
        Root = $RootName
        Path = $RelativePath
        Hash = Get-FileSha256 $File.FullName
      }
    }
  }

  return @($Entries | Sort-Object Root, Path)
}

function Read-InstallManifest {
  param([string]$Path, [System.Collections.IDictionary]$ManagedRoots)

  $Entries = @{}
  if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    Write-Step "No previous managed-file manifest found; existing unlisted files will be preserved."
    return $Entries
  }

  $LineNumber = 0
  foreach ($Line in Get-Content -LiteralPath $Path) {
    $LineNumber++
    if ([string]::IsNullOrWhiteSpace($Line) -or $Line.StartsWith('#')) {
      continue
    }

    $Parts = $Line -split "`t"
    if ($Parts.Count -ne 3) {
      throw "Malformed managed-file manifest at ${Path}:$LineNumber"
    }

    $RootName, $RelativePath, $Hash = $Parts
    if (-not $ManagedRoots.Contains($RootName)) {
      throw "Unknown managed-file root '$RootName' at ${Path}:$LineNumber"
    }
    Assert-SafeManifestRelativePath $RelativePath
    if ($Hash -notmatch '^[a-fA-F0-9]{64}$') {
      throw "Invalid SHA-256 at ${Path}:$LineNumber"
    }

    $Key = "$RootName/$RelativePath"
    if ($Entries.ContainsKey($Key)) {
      throw "Duplicate managed-file manifest entry '$Key' at ${Path}:$LineNumber"
    }

    $Entries[$Key] = [pscustomobject]@{
      Root = $RootName
      Path = $RelativePath
      Hash = $Hash.ToLowerInvariant()
    }
  }

  return $Entries
}

function Assert-ManagedFilesMatch {
  param([array]$Entries, [System.Collections.IDictionary]$ManagedRoots)

  if ($DryRun) {
    Write-Step "[dry-run] Would verify $($Entries.Count) managed files against repository SHA-256 hashes."
    return
  }

  foreach ($Entry in $Entries) {
    $Destination = Get-ManagedDestination $ManagedRoots $Entry.Root $Entry.Path
    if (-not (Test-Path -LiteralPath $Destination -PathType Leaf)) {
      throw "Managed file was not installed: $Destination"
    }
    if ((Get-FileSha256 $Destination) -ne $Entry.Hash) {
      throw "Managed file does not match the repository source: $Destination"
    }
  }

  Write-Step "OK managed-file content: $($Entries.Count)/$($Entries.Count) exact SHA-256 matches"
}

function Retire-StaleManagedFiles {
  param([hashtable]$PreviousEntries, [array]$CurrentEntries, [System.Collections.IDictionary]$ManagedRoots)

  $CurrentKeys = @{}
  foreach ($Entry in $CurrentEntries) {
    $CurrentKeys["$($Entry.Root)/$($Entry.Path)"] = $true
  }

  foreach ($Key in @($PreviousEntries.Keys | Sort-Object)) {
    if ($CurrentKeys.ContainsKey($Key)) {
      continue
    }

    $Entry = $PreviousEntries[$Key]
    $Destination = Get-ManagedDestination $ManagedRoots $Entry.Root $Entry.Path
    if (-not (Test-Path -LiteralPath $Destination -PathType Leaf)) {
      Write-Step "Formerly managed file already absent: $Destination"
      continue
    }

    if ((Get-FileSha256 $Destination) -ne $Entry.Hash) {
      Write-Warning "Preserving customized formerly managed file: $Destination"
      continue
    }

    Backup-File $Destination
    Write-Step "Retiring formerly managed file: $Destination"
    Invoke-InstallCommand { Remove-Item -LiteralPath $Destination -Force } "Remove-Item '$Destination'"
  }
}

function Write-InstallManifest {
  param([array]$Entries, [string]$Path)

  $Lines = @('# coding-agent-playbook-codex managed files v1')
  foreach ($Entry in $Entries) {
    $Lines += "$($Entry.Root)`t$($Entry.Path)`t$($Entry.Hash)"
  }
  $Content = ($Lines -join "`n") + "`n"

  if (Test-Path -LiteralPath $Path -PathType Leaf) {
    $Existing = (Get-Content -LiteralPath $Path -Raw) -replace "`r`n", "`n"
    if ($Existing -eq $Content) {
      Write-Step "Unchanged $Path"
      return
    }
  }

  $Parent = Split-Path -Parent $Path
  Invoke-InstallCommand { New-Item -ItemType Directory -Force -Path $Parent | Out-Null } "New-Item -ItemType Directory -Force '$Parent'"
  Backup-File $Path
  Write-Step "Writing managed-file manifest: $Path"
  if ($DryRun) {
    Write-Step "[dry-run] Would write $($Entries.Count) managed-file entries."
  } else {
    [System.IO.File]::WriteAllText($Path, $Content, [System.Text.UTF8Encoding]::new($false))
  }
}

function Retire-LegacyManifest {
  param([string]$LegacyPath)

  if (-not (Test-Path -LiteralPath $LegacyPath -PathType Leaf)) {
    return
  }

  Backup-File $LegacyPath
  Write-Step "Retiring legacy managed-file manifest: $LegacyPath"
  Invoke-InstallCommand { Remove-Item -LiteralPath $LegacyPath -Force } "Remove-Item '$LegacyPath'"
}

function Get-ExactMarkerMatches {
  param([string]$Text, [string]$Marker)

  $Pattern = "(?m)^" + [regex]::Escape($Marker) + "`r?$"
  return @([regex]::Matches($Text, $Pattern))
}

function AddOrReplace-PlaybookSection {
  param([string]$Target, [string]$Body)

  $StartMarker = "<!-- coding-agent-playbook-codex:start -->"
  $EndMarker = "<!-- coding-agent-playbook-codex:end -->"
  $LegacyStartMarker = "<!-- codex-agent-playbook:start -->"
  $LegacyEndMarker = "<!-- codex-agent-playbook:end -->"
  $Parent = Split-Path -Parent $Target
  $Newline = "`n"
  $NormalizedBody = ($Body -replace "`r`n", "`n") -replace "`r", "`n"
  $NormalizedBody = ($NormalizedBody -replace "`n+\z", "") + "`n"
  $Section = "$StartMarker$Newline$NormalizedBody$EndMarker"

  if (Test-Path -LiteralPath $Target -PathType Leaf) {
    $Existing = Get-Content -LiteralPath $Target -Raw
    $Newline = if ($Existing.Contains("`r`n")) { "`r`n" } else { "`n" }
    if ($Newline -eq "`r`n") {
      $NormalizedBody = $NormalizedBody -replace "`n", "`r`n"
    }
    $Section = "$StartMarker$Newline$NormalizedBody$EndMarker"
    $CurrentStarts = @(Get-ExactMarkerMatches $Existing $StartMarker)
    $CurrentEnds = @(Get-ExactMarkerMatches $Existing $EndMarker)
    $LegacyStarts = @(Get-ExactMarkerMatches $Existing $LegacyStartMarker)
    $LegacyEnds = @(Get-ExactMarkerMatches $Existing $LegacyEndMarker)
    $HasAnyMarker = $CurrentStarts.Count -gt 0 -or $CurrentEnds.Count -gt 0 -or $LegacyStarts.Count -gt 0 -or $LegacyEnds.Count -gt 0

    if ($HasAnyMarker) {
      $CurrentPairValid = $CurrentStarts.Count -eq 1 -and $CurrentEnds.Count -eq 1 -and $CurrentEnds[0].Index -gt $CurrentStarts[0].Index
      $LegacyPairValid = $LegacyStarts.Count -eq 1 -and $LegacyEnds.Count -eq 1 -and $LegacyEnds[0].Index -gt $LegacyStarts[0].Index
      $CurrentPairAbsent = $CurrentStarts.Count -eq 0 -and $CurrentEnds.Count -eq 0
      $LegacyPairAbsent = $LegacyStarts.Count -eq 0 -and $LegacyEnds.Count -eq 0

      if ((-not $CurrentPairValid -and -not $CurrentPairAbsent) -or
          (-not $LegacyPairValid -and -not $LegacyPairAbsent) -or
          ($CurrentPairValid -and $LegacyPairValid)) {
        throw "Malformed Coding Agent Playbook — Codex Edition markers in $Target; no changes were made."
      }

      if ($CurrentPairValid) {
        $ActiveStartMatch = $CurrentStarts[0]
        $ActiveEndMatch = $CurrentEnds[0]
      } else {
        $ActiveStartMatch = $LegacyStarts[0]
        $ActiveEndMatch = $LegacyEnds[0]
        Write-Step "Migrating legacy Coding Agent Playbook markers in $Target"
      }

      $Updated = $Existing.Substring(0, $ActiveStartMatch.Index) + $Section + $Existing.Substring($ActiveEndMatch.Index + $ActiveEndMatch.Length)
      if ($Updated -eq $Existing) {
        Write-Step "Unchanged $Target"
        return
      }

      Backup-File $Target
      if ($DryRun) {
        Write-Step "[dry-run] Would replace the Coding Agent Playbook — Codex Edition section in $Target"
      } else {
        Set-Content -LiteralPath $Target -Value $Updated -Encoding UTF8 -NoNewline
      }
      return
    }
  }

  Invoke-InstallCommand { New-Item -ItemType Directory -Force -Path $Parent | Out-Null } "New-Item -ItemType Directory -Force '$Parent'"
  Backup-File $Target

  if ($DryRun) {
    Write-Step "[dry-run] Would append the Coding Agent Playbook — Codex Edition section to $Target"
  } else {
    if (Test-Path -LiteralPath $Target -PathType Leaf) {
      Set-Content -LiteralPath $Target -Value ($Existing + $Newline + $Newline + $Section) -Encoding UTF8 -NoNewline
    } else {
      Set-Content -LiteralPath $Target -Value $Section -Encoding UTF8 -NoNewline
    }
  }
}

function Remove-PlaybookSection {
  param([string]$Target)

  if (-not (Test-Path -LiteralPath $Target -PathType Leaf)) {
    Write-Step "No playbook-owned global section to remove: $Target"
    return
  }

  $StartMarker = "<!-- coding-agent-playbook-codex:start -->"
  $EndMarker = "<!-- coding-agent-playbook-codex:end -->"
  $LegacyStartMarker = "<!-- codex-agent-playbook:start -->"
  $LegacyEndMarker = "<!-- codex-agent-playbook:end -->"
  $Existing = Get-Content -LiteralPath $Target -Raw
  $CurrentStarts = @(Get-ExactMarkerMatches $Existing $StartMarker)
  $CurrentEnds = @(Get-ExactMarkerMatches $Existing $EndMarker)
  $LegacyStarts = @(Get-ExactMarkerMatches $Existing $LegacyStartMarker)
  $LegacyEnds = @(Get-ExactMarkerMatches $Existing $LegacyEndMarker)
  $HasAnyMarker = $CurrentStarts.Count -gt 0 -or $CurrentEnds.Count -gt 0 -or $LegacyStarts.Count -gt 0 -or $LegacyEnds.Count -gt 0

  if (-not $HasAnyMarker) {
    Write-Step "No playbook-owned global section to remove: $Target"
    return
  }

  $CurrentPairValid = $CurrentStarts.Count -eq 1 -and $CurrentEnds.Count -eq 1 -and $CurrentEnds[0].Index -gt $CurrentStarts[0].Index
  $LegacyPairValid = $LegacyStarts.Count -eq 1 -and $LegacyEnds.Count -eq 1 -and $LegacyEnds[0].Index -gt $LegacyStarts[0].Index
  $CurrentPairAbsent = $CurrentStarts.Count -eq 0 -and $CurrentEnds.Count -eq 0
  $LegacyPairAbsent = $LegacyStarts.Count -eq 0 -and $LegacyEnds.Count -eq 0

  if ((-not $CurrentPairValid -and -not $CurrentPairAbsent) -or
      (-not $LegacyPairValid -and -not $LegacyPairAbsent) -or
      ($CurrentPairValid -and $LegacyPairValid)) {
    throw "Malformed Coding Agent Playbook — Codex Edition markers in $Target; no changes were made."
  }

  if ($CurrentPairValid) {
    $ActiveStartMatch = $CurrentStarts[0]
    $ActiveEndMatch = $CurrentEnds[0]
  } else {
    $ActiveStartMatch = $LegacyStarts[0]
    $ActiveEndMatch = $LegacyEnds[0]
  }

  $Updated = $Existing.Substring(0, $ActiveStartMatch.Index) + $Existing.Substring($ActiveEndMatch.Index + $ActiveEndMatch.Length)
  Backup-File $Target
  if ($DryRun) {
    Write-Step "[dry-run] Would remove the Coding Agent Playbook — Codex Edition section from $Target"
  } else {
    Set-Content -LiteralPath $Target -Value $Updated -Encoding UTF8 -NoNewline
    Write-Step "Removed the Coding Agent Playbook — Codex Edition section from $Target"
  }
}

$GlobalInstructions = Join-Path $RepoRoot "custom-instructions\global-coding-agent-instructions.md"
$AgentsDir = Join-Path $RepoRoot "agents"
$TargetAgentsMd = Join-Path $CodexHome "AGENTS.md"
$ManagedRoots = [ordered]@{
  references = @{ Destination = (Join-Path $CodexHome "references") }
  agents = @{ Source = $AgentsDir; Destination = (Join-Path $CodexHome "agents") }
  skills = @{ Destination = $LegacyUserSkillsHome }
}
$CurrentManagedRoots = [ordered]@{
  agents = $ManagedRoots['agents']
}

Write-Step "Coding Agent Playbook — Codex Edition companion installer"
Write-Step "Mode: $Mode"
Write-Step "Repository: $RepoRoot"
Write-Step "CODEX_HOME: $CodexHome"
Write-Step "Legacy user skills location (retirement only): $LegacyUserSkillsHome"
Write-Step "Managed-file manifest: $ManifestPath"

if (-not (Test-Path -LiteralPath $GlobalInstructions -PathType Leaf)) {
  throw "Missing global instructions: $GlobalInstructions"
}

$CurrentManifestEntries = Get-CurrentManifestEntries $CurrentManagedRoots
$PreviousManifestPath = if (Test-Path -LiteralPath $ManifestPath -PathType Leaf) { $ManifestPath } elseif (Test-Path -LiteralPath $LegacyManifestPath -PathType Leaf) { $LegacyManifestPath } else { $ManifestPath }
if ($PreviousManifestPath -eq $LegacyManifestPath) {
  Write-Step "Migrating legacy managed-file manifest: $LegacyManifestPath"
}
$PreviousManifestEntries = Read-InstallManifest $PreviousManifestPath $ManagedRoots

$OverrideAgentsMd = Join-Path $CodexHome "AGENTS.override.md"
if ($Mode -eq "full" -and
    (Test-Path -LiteralPath $OverrideAgentsMd -PathType Leaf) -and
    -not [string]::IsNullOrWhiteSpace((Get-Content -LiteralPath $OverrideAgentsMd -Raw))) {
  throw "Non-empty $OverrideAgentsMd takes precedence over AGENTS.md. Full mode stopped before making changes. Reconcile or remove the override, or use -SupportOnly for custom agents without global guidance."
}

if ($Mode -eq "full") {
  $Body = Get-Content -LiteralPath $GlobalInstructions -Raw
  AddOrReplace-PlaybookSection $TargetAgentsMd $Body
} else {
  Remove-PlaybookSection $TargetAgentsMd
}

Copy-PlaybookTree $AgentsDir $ManagedRoots['agents'].Destination
Assert-ManagedFilesMatch $CurrentManifestEntries $ManagedRoots
Retire-StaleManagedFiles $PreviousManifestEntries $CurrentManifestEntries $ManagedRoots
Write-InstallManifest $CurrentManifestEntries $ManifestPath
Retire-LegacyManifest $LegacyManifestPath

Write-Step ""
Write-Step "Validation:"
$CheckPaths = @(
  (Join-Path $CodexHome "agents\planner.toml"),
  (Join-Path $CodexHome "agents\engineer.toml"),
  (Join-Path $CodexHome "agents\reviewer.toml"),
  (Join-Path $CodexHome "agents\tester.toml"),
  (Join-Path $CodexHome "agents\docs.toml"),
  (Join-Path $CodexHome "agents\planner-luna.toml"),
  (Join-Path $CodexHome "agents\engineer-luna.toml"),
  (Join-Path $CodexHome "agents\reviewer-luna.toml"),
  (Join-Path $CodexHome "agents\tester-luna.toml"),
  (Join-Path $CodexHome "agents\docs-luna.toml")
)

if ($Mode -eq "full") {
  $CheckPaths = @($TargetAgentsMd) + $CheckPaths
}

foreach ($Path in $CheckPaths) {
  if ($DryRun -or (Test-Path -LiteralPath $Path)) {
    Write-Step "OK: $Path"
  } else {
    Write-Warning "Missing: $Path"
  }
}

Write-Step ""
Write-Step "Companion install complete. Skills and references remain provided by the Codex plugin. Restart Codex or start a new task if needed so updated instructions and agents are loaded."
