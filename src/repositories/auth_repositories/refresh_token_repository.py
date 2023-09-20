from typing import Any
from fastapi import HTTPException
from src.models.model import Credential
from sqlalchemy.exc import SQLAlchemyError
from src.configurations.databases.postgresql import Session

# Refresh Token Repository
class refresh_token_repo:
    __CONNECTION = Session()

    # Refresh Token Repository
    def refresh_token(self, user_id: str) -> str:
        try:
            credential_is_exist: Any = self.__CONNECTION.query(Credential).filter_by(
                owner_id = user_id
            ).first()

            if credential_is_exist is None:
                return ""

            return credential_is_exist.owner_id

        except SQLAlchemyError as error_message:
            print(error_message)
            raise HTTPException(
                status_code = 500,
                detail = 'Internal Server Error'
            )