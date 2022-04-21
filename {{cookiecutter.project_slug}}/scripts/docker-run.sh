#!/usr/bin/env bash

ACTUAL_DIR=${0%/*}
cd "${ACTUAL_DIR}/../"

docker run --rm -p 8080:80 --name {{cookiecutter.project_slug}}-container {{cookiecutter.project_slug}}