from src.services.auth_services import (
    login_service,
    register_service,
    refresh_token_service
)

#  Auth Services
class auth_services(
    login_service.login_svc,
    register_service.register_svc,
    refresh_token_service.refresh_token_svc
) :

    def __init__(self) -> None:
        super().__init__()
        