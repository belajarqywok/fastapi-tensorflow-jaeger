import os
from dotenv import load_dotenv

from sqlalchemy import Engine, engine, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

# Postgres Engines Options
class Engines:
    def __init__(self) -> None:
        # IP Engine
        self.ip_engine: Engine = create_engine(
            url = (
                f'postgresql+psycopg2://' +
                f'{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASS")}' +
                f'@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/' +
                f'{os.getenv("POSTGRES_DB")}'
            )
        )

        # UNIX Socket Engine
        self.unix_sock_engine: Engine = create_engine(
            engine.url.URL.create(
                drivername = "postgresql+psycopg2",
                username = {os.getenv("POSTGRES_USER")},
                password = {os.getenv("POSTGRES_PASS")},
                database = {os.getenv("POSTGRES_DB")},
                query = {
                    "unix_sock": (
                        f'{os.getenv("POSTGRES_HOST")}' + 
                        f'/.s.PGSQL.{os.getenv("POSTGRES_PORT")}'
                    )
                }
            )
        )

# Session
engine: Engine = Engines().ip_engine
Session: sessionmaker[Session] = sessionmaker(
    autoflush  = False,
    autocommit = False,
    bind = engine
)

# Base
Base = declarative_base()
