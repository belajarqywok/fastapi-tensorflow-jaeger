import os
from dotenv import load_dotenv

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

# Create Engine
engine: Engine = create_engine(
    url = (
        f'postgresql+psycopg2://' +
        f'{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASS")}' +
        f'@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/' +
        f'{os.getenv("POSTGRES_DB")}'
    )
)

# Session
Session: sessionmaker[Session] = sessionmaker(
    autoflush  = False,
    autocommit = False,
    bind = engine
)

# Base
Base = declarative_base()
