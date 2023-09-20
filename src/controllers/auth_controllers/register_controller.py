from http import HTTPStatus
from fastapi.responses import JSONResponse
from src.services.auth_services import auth_services
from src.schemas.user_request_schema import RegisterRequestSchema

# Register Controller
class register_controller:
    # Auth Service
    __SERVICE = auth_services()

    # Register Controller
    def register(self, payload: RegisterRequestSchema) -> JSONResponse:
        try: 
            register_service: bool = self.__SERVICE.register(
                payload = payload
            )

            if not register_service :
                return JSONResponse(
                    content = {
                        'message': 'Register Failed',
                        'status_code': HTTPStatus.BAD_REQUEST,
                        'data': None
                    },
                    status_code = HTTPStatus.BAD_REQUEST
                )

            return JSONResponse(
                content = {
                    'message': 'Register Success',
                    'status_code': HTTPStatus.CREATED,
                    'data': None
                },
                status_code = HTTPStatus.CREATED
            )

        except Exception as error_message:
            print(error_message)
            return JSONResponse(
                content = {
                    'message': 'Internal Server Error',
                    'status_code': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'data': None
                },
                status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            )
