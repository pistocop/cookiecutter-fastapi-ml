#!/usr/bin/env bash

set -e

OLD_DIR=$(pwd)
ACTUAL_DIR=${0%/*}
MODELS_JSON="app/ml-models.json"
MODELS_DEST_PATH="app/ml-models/"

# Check required programs
if ! command -v jq &> /dev/null
then
    echo "'jq' program required but not found"
    exit
fi

# Load info usefull to download the models from two files:
# 1. From $MODELS_JSON the models link
# 2. From .env the secrets usefull to download the models
if [ -f src/.env ]
then
    source src/.env
fi

# jq iteration from: https://www.starkandwayne.com/blog/bash-for-loop-over-json-array-using-jq/
for row in $(cat "${MODELS_JSON}" | jq -r '.[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }
    MODEL_ID="$(_jq '.model_id')"
    MODEL_LINK="$(_jq '.download_link')"
    MODEL_PATH="${MODELS_DEST_PATH}"/"${MODEL_ID}"
    echo "Downloading model $MODEL_ID from link $MODEL_LINK and store to $MODEL_PATH"
    # <your download mechanism here>, you could use .env info (e.g. $MY_SECRET_TOKEN)
done

echo "All models downloaded!"
