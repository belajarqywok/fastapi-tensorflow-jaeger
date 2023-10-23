from src.controllers.main_controllers import (
    main_controller,
    liveness_check_controller,
    readiness_check_controller
)

# Main Controllers
class main_controllers(
    main_controller.main_controller,
    liveness_check_controller.liveness_check_controller,
    readiness_check_controller.readiness_check_controller
):

    def __init__(self) -> None:
        super().__init__()