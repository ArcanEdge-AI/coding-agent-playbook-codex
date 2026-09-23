#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for python_command in python3 python; do
  if command -v "$python_command" >/dev/null 2>&1; then
    exec "$python_command" "$SCRIPT_DIR/install.py" "$@"
  fi
done

echo "Python 3 is required. Install Python 3 or run install/install.py with an available Python 3 interpreter." >&2
exit 1
