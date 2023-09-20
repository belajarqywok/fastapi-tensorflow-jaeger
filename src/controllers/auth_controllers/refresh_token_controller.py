from http import HTTPStatus
from typing import Any, Dict
from fastapi.responses import JSONResponse

from src.services.auth_services import auth_services
from src.schemas.user_request_schema import RefreshRequestSchema

# Refresh Token Controller
class refresh_token_controller:
    # Auth Service
    __SERVICE = auth_services()

    # Refresh Token Controller
    def refresh_token(self, payload: RefreshRequestSchema) -> JSONResponse:
        try:
            # Refresh Token Service 
            refresh_token_service: Dict[str, Any] = self.__SERVICE.refresh_token(
                payload = payload.__dict__
            )

            if refresh_token_service['data'] is None :
                return JSONResponse(
                    content = {
                        'message': 'Token Invalid',
                        'status_code': HTTPStatus.BAD_REQUEST,
                        'data': None
                    },
                    status_code = HTTPStatus.BAD_REQUEST
                )

            return JSONResponse(
                content = {
                    'message': 'Refresh Token Success',
                    'status_code': HTTPStatus.OK,
                    'data': refresh_token_service['data']
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
