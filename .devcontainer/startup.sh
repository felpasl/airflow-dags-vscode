#!/bin/bash
# Create and activate Python virtual environment, then install requirements

VENV_DIR="/opt/airflow/.venv"
REQ_FILE="/opt/airflow/requirements.txt"

# Create virtual environment if not exists
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r "$REQ_FILE"

echo "Virtual environment activated and requirements installed."

echo "Running Airflow database migrations..."
airflow db migrate

echo "Airflow database initialized successfully."

echo "Create Postgres conection"

airflow connections add 'postgres_default' \
  --conn-type 'postgres' \
  --conn-host 'postgres' \
  --conn-login 'postgres' \
  --conn-password 'postgres' \
  --conn-schema 'airflow' \
  --conn-port '5432'

