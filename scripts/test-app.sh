#!/usr/bin/env bash

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}"/../

pytest ./tests/