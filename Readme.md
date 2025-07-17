
# Apache Airflow Dev Container Project

## Summary

This project provides a ready-to-use [dev container](https://containers.dev/) environment for developing with [Apache Airflow](https://airflow.apache.org/) using Docker Compose. It is pre-configured for local development with a PostgreSQL backend and includes essential tools for Python development. Debugging and developing Airflow DAGs is streamlined with VS Code integration.

**Key Features:**
- Isolated, reproducible development using VS Code Dev Containers
- Pre-installed Python and Airflow with PostgreSQL backend
- Automated setup and initialization
- Debugging support for Airflow DAGs in VS Code
- Recommended extensions for Python and SQL

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Configuration Details](#configuration-details)
4. [Debugging Airflow DAGs](#debugging-airflow-dags)
5. [Customization](#customization)
6. [Useful Commands](#useful-commands)
7. [Troubleshooting](#troubleshooting)
8. [References](#references)

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [VS Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Quick Start

1. **Clone this repository** to your local machine.
2. **Open the folder in VS Code**.
3. **Reopen in Container**: When prompted, or via the Command Palette (`Ctrl+Shift+P` > "Dev Containers: Reopen in Container").
4. **Wait for setup**: The container will build, install dependencies, and initialize Airflow.
5. **Access Airflow UI**: Open [http://localhost:8080](http://localhost:8080) in your browser.
   - Default credentials:  
     - Username: `admin`  
     - Password: `admin`  
     (Create with the command below if not present.)

---

## Project Structure

- `.devcontainer/`: Dev container configuration files.
  - `devcontainer.json`: Main dev container settings.
  - `docker-compose.yaml`: Defines Airflow and PostgreSQL services.
  - `startup.sh`: Bootstraps the Python environment and Airflow.
- `dags/`: Place your Airflow DAGs here.
- `requirements.txt`: Python dependencies for Airflow and your DAGs.
- `.vscode/launch.json`: Debug configuration for Airflow DAGs.

---

## Configuration Details

### Airflow

- **DAGs Folder**: `/opt/airflow/dags`
- **Database**: PostgreSQL, service name `postgres`, database `airflow`
- **Connection**: A default connection named `postgres_default` is created for use in DAGs.

### Dev Container

- **Python**: Uses a virtual environment at `/opt/airflow/.venv`
- **Ports Exposed**:
  - 8080: Airflow Webserver
  - 5432: PostgreSQL

### VS Code Extensions

Recommended extensions are automatically installed, including Python, Pylance, SQLTools, and Docker.

---

## Debugging Airflow DAGs

### Debugging the Sample DAG

This project includes a sample DAG located at `dags/sampledag.py`. To debug this DAG using VS Code:

1. Ensure your Python environment and dependencies are set up (see `requirements.txt`).
2. Open the workspace in VS Code.
3. Use the provided launch configuration:
   - Go to the Run and Debug panel (Ctrl+Shift+D).
   - Select **Debug Airflow DAG (sample_dag)**.
   - Start debugging. This will launch Airflow using the `.venv` environment.
4. Set breakpoints in your DAG file as needed.

### Creating and Debugging Other DAGs

To add and debug new DAGs:

1. Create a new Python file in the `dags/` directory (e.g., `dags/my_new_dag.py`).
2. Define your DAG following [Airflow's documentation](https://airflow.apache.org/docs/).
3. (Optional) Add a new debug configuration in `.vscode/launch.json` for your DAG if you want a dedicated launch option.
4. Set breakpoints and use the debugger as described above.

**Tip:** You can use the same debug configuration for any DAG, as Airflow will discover all DAGs in the `dags/` folder.

---

## Customization

- **Python dependencies**: Add to `requirements.txt`.
- **Airflow connections**: Modify `startup.sh` or use Airflow CLI.
- **Environment variables**: Adjust in `.devcontainer/docker-compose.yaml` or `.env`.

---

## Useful Commands

- **Start Airflow webserver**:  
  `airflow webserver`
- **Start Airflow scheduler**:  
  `airflow scheduler`
- **List DAGs**:  
  `airflow dags list`
- **Test a DAG**:  
  `airflow dags test <dag_id> <execution_date>`

---

## Troubleshooting

- If you encounter issues with dependencies, rebuild the container (`Dev Containers: Rebuild Container`).
- Ensure Docker is running and ports are not in use by other services.

---

## References

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
- [Docker Compose](https://docs.docker.com/compose/)

---

Happy developing!
