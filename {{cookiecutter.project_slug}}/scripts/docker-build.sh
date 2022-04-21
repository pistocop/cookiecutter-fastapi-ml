#!/usr/bin/env bash

set -e

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}/../"

docker build -t {{cookiecutter.project_slug}} .