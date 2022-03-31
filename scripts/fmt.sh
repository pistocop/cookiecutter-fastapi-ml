#!/usr/bin/env bash

set -e
set -x

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}"/../

black app/
isort app/
flake8 app/
