#!/usr/bin/env bash

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}/../"

docker run --rm -p 8000:80 --name be-fastapi-ml-container be-fastapi-ml