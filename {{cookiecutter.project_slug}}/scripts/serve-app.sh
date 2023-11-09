#!/usr/bin/env bash

set -e
set -x

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}"/../

PORT=${1:-8080}

# Launch using uvicorn:
uvicorn --reload --host=0.0.0.0 --port="$PORT" app.main:app

# Launch using python `main.py`:
# export PYTHONPATH="$PWD" && python app/main.py