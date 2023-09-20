from http import HTTPStatus
from typing import Any, Dict
from fastapi.responses import JSONResponse
from src.services.auth_services import auth_services
from src.schemas.user_request_schema import LoginRequestSchema

# Login Controller
class login_controller:
    # Auth Service
    __SERVICE = auth_services()

    # Login Controller
    def login(self, payload: LoginRequestSchema) -> JSONResponse:
        try: 
            login_service: Dict[str, Any] = self.__SERVICE.login(
                payload = payload
            )

            if login_service['data'] == None :
                return JSONResponse(
                    content = {
                        'message': 'Login Failed',
                        'status_code': HTTPStatus.FORBIDDEN,
                        'data': None
                    },
                    status_code = HTTPStatus.FORBIDDEN
                )

            return JSONResponse(
                content = {
                    'message': 'Login Success',
                    'status_code': HTTPStatus.OK,
                    'data': login_service['data']
                },
                status_code = HTTPStatus.OK
            )

        except Exception as error_message :
            print(error_message)
            return JSONResponse(
                content = {
                    'message': 'Internal Server Error',
                    'status_code': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'data': None
                },
                status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            )
