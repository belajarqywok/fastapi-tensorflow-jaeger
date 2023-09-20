from src.controllers.auth_controllers import (
    login_controller,
    register_controller,
    refresh_token_controller
)

# Auth Controllers
class auth_controllers(
    login_controller.login_controller,
    register_controller.register_controller,
    refresh_token_controller.refresh_token_controller
):

    def __init__(self) -> None:
        super().__init__()