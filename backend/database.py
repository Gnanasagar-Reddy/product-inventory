import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

load_dotenv(Path(__file__).resolve().parent.parent / '.env')

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=os.environ["DB_PASSWORD"],
    host="localhost",
    port=5432,
    database="fastapi_tut",
)

engine = create_engine(db_url)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)