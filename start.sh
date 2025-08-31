#!/bin/sh

TRUNCATE=$1
VENV_DIR="venv"
REQ_FILE="requirements.txt"

if [ -z "$SHELLED" ]; then
    export SHELLED=1
    exec "$SHELL" "$0" "$@"
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment.."
    python3 -m venv "$VENV_DIR"
fi

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment.."
    . "$VENV_DIR/bin/activate"
fi

if [ -f "$REQ_FILE" ]; then
    echo "Checking/installing dependencies.."
    pip install -r "$REQ_FILE"
fi

if [ "$TRUNCATE" = "y" ]; then
    python3 ./src/main.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g' > logs/out.log
elif [ "$TRUNCATE" = "n" ]; then
    python3 ./src/main.py 2>&1 | sed 's/\x1b\[[0-9;]*m//g' >> logs/out.log
else
    echo "Usage: ./start.sh <y|n> (truncate logs)"
    exit 1
fi

