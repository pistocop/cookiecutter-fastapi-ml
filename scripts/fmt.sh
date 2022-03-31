#!/usr/bin/env bash

set -e
set -x

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}"/../

black app/ tests/
isort app/ tests/
flake8 app/ tests/
