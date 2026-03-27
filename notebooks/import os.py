import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# Load local .env.cricbuzz for local development
load_dotenv(dotenv_path=Path("../.env.cricbuzz"), override=True)

# Get MySQL credentials from environment
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PWD")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
database = os.getenv("MYSQL_DB")


engine = create_engine(
    f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
.to_sql(name="", con=engine, if_exists="replace", index=False)

print(
    f"Data uploaded to MySQL successfully, Database: {database}, Table: indian_player")
