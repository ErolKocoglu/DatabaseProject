# Database Project

This is a Flask-based web application for managing football data (clubs, players, games, etc.).

## Prerequisites

- Python 3.x
- PostgreSQL

## Database Setup

The project is configured to connect to a PostgreSQL database with the following credentials (hardcoded in `database.py`):

- **Host**: `localhost`
- **User**: `postgres`
- **Password**: `12345678`
- **Database Name**: `DatabaseProject`

### Steps to Initialize Database:

1.  Make sure PostgreSQL is running.
2.  Create a database named `DatabaseProject`.
3.  Ensure the `postgres` user has the password `12345678` (or update `DatabaseProject/database.py` with your credentials).
4.  Run the provided SQL scripts in the `DatabaseProject` subdirectory to set up the schema and data:
    ```bash
    psql -U postgres -d DatabaseProject -f DatabaseProject/database.sql
    psql -U postgres -d DatabaseProject -f DatabaseProject/dataset.sql
    ```
    *(Adjust the command if you use a different way to run SQL files, e.g., pgAdmin).*

## Installation

1.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ./venv/Scripts/activate  # On Windows
    # source venv/bin/activate # On macOS/Linux
    ```

2.  Install the required dependencies:
    ```bash
    pip install flask flask-login flask-wtf psycopg2-binary
    ```

## Running the Application

1.  Navigate to the inner project directory:
    ```bash
    cd DatabaseProject
    ```

2.  Run the server:
    ```bash
    python server.py
    ```

3.  The application will start on port `8090` (as defined in `settings.py`).
    Access it at: [http://localhost:8090](http://localhost:8090)

## Accounts

There are predefined accounts in `settings.py`:
- **Admin**: user `admin` (Setup with a hashed password)
- **User**: user `normaluser` / password `abcd123`
