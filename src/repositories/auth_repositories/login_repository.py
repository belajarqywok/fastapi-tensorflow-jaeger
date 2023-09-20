from typing import Any
from fastapi import HTTPException
from src.models.model import Credential
from sqlalchemy.exc import SQLAlchemyError
from src.configurations.databases.postgresql import Session
from src.schemas.user_request_schema import LoginRequestSchema

# Login Repository
class login_repo:
    __CONNECTION = Session()

    def login(self, schema: LoginRequestSchema) -> str:
        try:
            credential_is_exist: Any = self.__CONNECTION.query(Credential).filter_by(
                email = schema.email,
                password = schema.password
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
