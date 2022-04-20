#!/usr/bin/env bash

set -e
set -x

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}"/../

pytest ./tests/