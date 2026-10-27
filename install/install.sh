#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for python_command in python3 python; do
  if command -v "$python_command" >/dev/null 2>&1; then
    exec "$python_command" "$SCRIPT_DIR/install.py" "$@"
  fi
done

echo "Python 3.8 or newer is required. Install it or run install/install.py with a compatible interpreter." >&2
exit 1
