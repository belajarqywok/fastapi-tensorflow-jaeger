from typing import Type
from datetime import datetime
from src.models.model import User, Credential
from src.configurations.security.jwt_utils import auth_utilities
from src.repositories.auth_repositories import auth_repositories
from src.schemas.user_request_schema import RegisterRequestSchema

# Register Service
class register_svc:
    # Repositories
    __REPOSITORY = auth_repositories()

    # Auth Utilities
    __AUTH_UTILS = auth_utilities()

    # Register Service
    def register(self, payload: RegisterRequestSchema) -> bool:
        current_datetime: Type[datetime] = datetime.now()
        formatted_datetime: str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Create the User and Credential instances
        profile: Type[User] = User(
            nickname  = payload.nickname,
            fullname  = payload.fullname,
            birthdate = payload.birth_date,
            createdAt = formatted_datetime,
            updatedAt = formatted_datetime
        )

        credential: Type[Credential] = Credential(
            owner = profile,
            email = payload.email,
            password = self.__AUTH_UTILS.password_hashing(
                plain_password = payload.password
            )
        )

        # repository response
        repo_response: bool = self.__REPOSITORY.register(
            profile = profile,
            credential = credential
        )

        return repo_response