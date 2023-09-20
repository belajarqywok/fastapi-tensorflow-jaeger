import os
from hashlib import sha512
from http import HTTPStatus
from dotenv import load_dotenv
from pydantic import BaseModel
from jose import jwt, exceptions
from src.models.model import User
from typing import Union, Any, Dict
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from fastapi import HTTPException, Security
from src.configurations.databases.postgresql import Session
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

load_dotenv()

# JWT Claims Model
class Claims(BaseModel):
    sub: str = None
    exp: int = None

class auth_utilities:
    # Database Session
    DATABASE: Session = Session()

    # Password Hashing
    def password_hashing(self, plain_password: str) -> str:
        hashing = sha512()
        hashing.update(plain_password.encode())
        return hashing.hexdigest()


    # Generate Access Token
    def generate_access_token(
        self,
        subject: Union[str, str],
        expires_delta: int = None
    ) -> str:
        if expires_delta is not None:
            expires_delta: int = datetime.utcnow() + expires_delta

        else :
            expires_delta: int = datetime.utcnow() + timedelta(
                hours = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE")) 
            )

        to_encode: Dict[str, Any] = {
            'sub': str(subject),
            'exp': expires_delta
        }

        encoded_jwt: str = jwt.encode(
            claims = to_encode, 
            key = os.getenv("JWT_ACCESS_TOKEN_SECRET"),
            algorithm = os.getenv("JWT_ALGORITHM")
        )

        return encoded_jwt


    # Generate Refresh Token
    def generate_refresh_token(
        self,
        subject: Union[str, str],
        expires_delta: int = None
    ) -> str:
        if expires_delta is not None:
            expires_delta: int = datetime.utcnow() + expires_delta

        else:
            expires_delta: int = datetime.utcnow() + timedelta(
                days = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE"))
            )

        to_encode: Dict[str, Any] = {
            'sub': str(subject),
            'exp': expires_delta
        }

        encoded_jwt: str = jwt.encode(
            claims = to_encode, 
            key = os.getenv("JWT_REFRESH_TOKEN_SECRET"),
            algorithm = os.getenv("JWT_ALGORITHM")
        )

        return encoded_jwt


    # Authorization
    def authorization(
        self,
        auth: HTTPAuthorizationCredentials = Security(dependency = HTTPBearer())
    ) -> str:
        try:
            payload = jwt.decode(
                token = auth.credentials,
                key = os.getenv("JWT_ACCESS_TOKEN_SECRET"),
                algorithms = [os.getenv("JWT_ALGORITHM")]
            )

            user_id: str = str(payload['sub'])
            
            user_id_is_exist: Any = self.DATABASE.query(User).filter_by(
                id = user_id
            ).first()

            if user_id_is_exist is None:
                raise JSONResponse(
                    content = {
                        'message': 'Token Invalid',
                        'status_code': HTTPStatus.FORBIDDEN,
                        'data': None
                    },
                    status_code = HTTPStatus.FORBIDDEN
                )

            return user_id

        except exceptions.ExpiredSignatureError:
            raise HTTPException(
                status_code = HTTPStatus.FORBIDDEN,
                detail = 'Token Invalid'
            )

        except exceptions.JWTError:
            raise HTTPException(
                status_code = HTTPStatus.FORBIDDEN,
                detail = 'Token Invalid'
            )