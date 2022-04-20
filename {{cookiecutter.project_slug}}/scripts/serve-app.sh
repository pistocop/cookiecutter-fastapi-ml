#!/usr/bin/env bash

set -e
set -x

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}"/../

# Launch using uvicorn:
uvicorn --reload --host=0.0.0.0 --port=8080 app.main:app

# Launch using python `main.py`:
# export PYTHONPATH="$PWD" && python app/main.py