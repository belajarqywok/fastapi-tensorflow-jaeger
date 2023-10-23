from http import HTTPStatus
from fastapi.responses import JSONResponse

# Main Controller
class main_controller:
    def main(self) -> JSONResponse:
        try: 
            return JSONResponse(
                content = {
                    'message': 'ML Service Running',
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