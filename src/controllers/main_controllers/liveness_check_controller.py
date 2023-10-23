from http import HTTPStatus
from fastapi.responses import JSONResponse

# Liveness Controller
class liveness_check_controller:
    def liveness_check(self) -> JSONResponse:
        try: 
            return JSONResponse(
                content = {
                    'message': 'Liveness Check Success',
                    'status_code': HTTPStatus.OK,
                    'data': None
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