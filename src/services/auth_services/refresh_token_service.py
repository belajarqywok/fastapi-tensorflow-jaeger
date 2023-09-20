import os
from jose import jwt
from typing import Dict
from datetime import datetime
from dotenv import load_dotenv
from src.configurations.security.jwt_utils import auth_utilities
from src.repositories.auth_repositories import auth_repositories

load_dotenv()

# Refresh Token Service
class refresh_token_svc:
    # Repositories
    __REPOSITORY = auth_repositories()

    # Auth Utilities
    __AUTH_UTILS = auth_utilities()

    # Refresh Token Service
    def refresh_token(self, payload: Dict[str, str]) -> dict:
        payload_decode = jwt.decode(
            token = payload['refresh_token'],
            key = os.getenv("JWT_REFRESH_TOKEN_SECRET"),
            algorithms = os.getenv("JWT_ALGORITHM")
        )

        if datetime.fromtimestamp(payload_decode['exp']) < datetime.now() :
            return {
                'data': None
            }

        repo_response: str = self.__REPOSITORY.refresh_token(
            user_id = payload_decode['sub']
        )

        if repo_response == "":
            return {
                'data': None
            }

        return {
            'data': {
                'access_token': self.__AUTH_UTILS.generate_access_token(
                    subject = repo_response
                ),

                'refresh_token': self.__AUTH_UTILS.generate_refresh_token(
                    subject = repo_response
                )
            }
        } 