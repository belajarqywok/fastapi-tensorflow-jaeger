import os
from dotenv import load_dotenv

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

# Create Engine
engine: Engine = create_engine(
    url = os.getenv("POSTGRES_URL")
)

# Session
Session: sessionmaker[Session] = sessionmaker(
    autoflush  = False,
    autocommit = False,
    bind = engine
)

# Base
Base = declarative_base()
