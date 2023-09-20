from src.repositories.auth_repositories import (
    login_repository,
    register_repository,
    refresh_token_repository
)

# Auth Repositories
class auth_repositories(
    login_repository.login_repo,
    register_repository.register_repo,
    refresh_token_repository.refresh_token_repo
):

    def __init__(self) -> None:
        super().__init__()
        