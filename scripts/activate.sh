#!/usr/bin/env bash

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "====================================="
echo " Production Airflow Project"
echo "====================================="

# Activate virtual environment
source "${PROJECT_ROOT}/.venv/bin/activate"

# Airflow Home
export AIRFLOW_HOME="${PROJECT_ROOT}/airflow"

# Prevent Python from creating .pyc files
export PYTHONDONTWRITEBYTECODE=1

# Better Python output
export PYTHONUNBUFFERED=1

echo
echo "Python      : $(python --version)"
echo "Pip         : $(pip --version | awk '{print $2}')"
echo "Airflow     : $(airflow version)"
echo "AIRFLOW_HOME: ${AIRFLOW_HOME}"
echo
echo "Environment Ready ✅"
