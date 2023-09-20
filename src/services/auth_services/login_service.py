from src.configurations.security.jwt_utils import auth_utilities
from src.repositories.auth_repositories import auth_repositories
from src.schemas.user_request_schema import LoginRequestSchema

# Login Service
class login_svc:
    # Repositories
    __REPOSITORY = auth_repositories()

    # Auth Utilities
    __AUTH_UTILS = auth_utilities()

    # Login Service
    def login(self, payload: LoginRequestSchema) -> dict:
        hashing_password: str = self.__AUTH_UTILS.password_hashing(
            plain_password = payload.password
        )

        login_payload: dict = {
            "email": payload.email,
            "password": hashing_password
        }

        repo_response: str = self.__REPOSITORY.login(
            schema = LoginRequestSchema(**login_payload)
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