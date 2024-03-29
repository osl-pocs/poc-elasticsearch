#!/usr/bin/env bash

# prepare the conda environment
is_conda_in_path=$(echo $PATH|grep -m 1 --count /opt/conda/)

if [ $is_conda_in_path == 0 ]; then
  export PATH="/opt/conda/condabin:/opt/conda/bin:$PATH"
  echo "[II] included conda to the PATH"
fi

echo "[II] activate rxiv-rest-api"
source activate rxiv-rest-api

pushd ..
pwd
if [[ "$ENV" != "dev" ]]; then
  poetry install --no-root --only main
else
  poetry install --no-root
fi
popd

if [ $# -ne 0 ]
  then
    echo "Running: ${@}"
    ${@}
fi
