"""
Centralized MySQL connection handling for Cricbuzz LiveStats.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=PROJECT_ROOT / ".env.cricbuzz", override=True)

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PWD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DB")

# Cricbuzz RapidAPI headers
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST", "cricbuzz-cricket.p.rapidapi.com")

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}


def get_engine():
    connection_string = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(connection_string, pool_pre_ping=True)


def run_query(query: str, params: dict = None) -> pd.DataFrame:
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn, params=params)


def execute_statement(statement: str, params: dict = None):
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text(statement), params or {})


def upload_dataframe(df: pd.DataFrame, table_name: str, if_exists: str = "replace"):
    engine = get_engine()
    df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)
    print(
        f"Data uploaded to MySQL successfully. Database: {DB_NAME}, Table: {table_name}")
