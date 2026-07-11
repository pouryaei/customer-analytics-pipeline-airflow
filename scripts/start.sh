#!/usr/bin/env bash

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

source "${PROJECT_ROOT}/.venv/bin/activate"

export AIRFLOW_HOME="${PROJECT_ROOT}/airflow"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1

hash -r

echo "====================================="
echo " Customer Analytics Pipeline"
echo "====================================="
echo "Project Root : ${PROJECT_ROOT}"
echo "Python       : $(which python)"
echo "Airflow      : $(which airflow)"
echo "Version      : $(airflow version)"
echo "AIRFLOW_HOME : ${AIRFLOW_HOME}"
echo "====================================="