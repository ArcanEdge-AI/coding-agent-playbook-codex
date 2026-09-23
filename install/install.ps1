param(
  [switch]$Full,
  [switch]$SupportOnly,
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"

if ($Full -and $SupportOnly) {
  throw "Choose either -Full or -SupportOnly, not both. Full mode is the default for installs and updates."
}

$Installer = Join-Path $PSScriptRoot "install.py"
$InstallerArgs = @($Installer)
if ($Full) { $InstallerArgs += "--full" }
if ($SupportOnly) { $InstallerArgs += "--support-only" }
if ($DryRun) { $InstallerArgs += "--dry-run" }

$Launchers = @(
  @{ Command = "py"; Prefix = @("-3") },
  @{ Command = "python"; Prefix = @() },
  @{ Command = "python3"; Prefix = @() }
)

foreach ($Launcher in $Launchers) {
  $Command = Get-Command $Launcher.Command -ErrorAction SilentlyContinue
  if (-not $Command) { continue }

  $PrefixArgs = @($Launcher.Prefix)
  & $Command.Source @PrefixArgs @InstallerArgs
  exit $LASTEXITCODE
}

throw "Python 3 is required. Install Python 3 or run install/install.py with an available Python 3 interpreter."
