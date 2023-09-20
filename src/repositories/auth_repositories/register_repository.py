from typing import Any
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from src.models.model import User, Credential
from src.configurations.databases.postgresql import Session

# Register Repository
class register_repo:
    # Database Connection
    __CONNECTION = Session()

    # Register Repository
    def register(self, profile: User, credential: Credential) -> bool:
        try:
            email_is_exist: Any = self.__CONNECTION.query(Credential).filter_by(
                email = credential.email
            ).first()

            if email_is_exist is not None:
                return False

            self.__CONNECTION.add_all([profile, credential])
            self.__CONNECTION.commit()
            return True

        except SQLAlchemyError as error_message:
            self.__CONNECTION.rollback()
            print(error_message)
            raise HTTPException(
                status_code = 500,
                detail = 'Internal Server Error'
            )

        except Exception as error_message:
            self.__CONNECTION.rollback()
            print(error_message)
            raise HTTPException(
                status_code = 500,
                detail = 'Internal Server Error'
            )