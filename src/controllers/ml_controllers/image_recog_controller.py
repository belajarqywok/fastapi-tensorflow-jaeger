from http import HTTPStatus
from fastapi.responses import JSONResponse
from fastapi import UploadFile, HTTPException
from src.services.ml_services.image_recog_service import image_recog_service

# Image Recog Controller
class image_recog_controller():
    # Image Recognition Service
    _IMAGE_RECOG_SERVICE = image_recog_service()

    # Image Predict
    async def image_predict(self, file: UploadFile) -> JSONResponse:
        # get the file size (in bytes)
        file.file.seek(0, 2)
        file_size = file.file.tell()

        # move the cursor back to the beginning
        await file.seek(0)
        if file_size > 10 * 1024 * 1024:
            # more than 10 MB
            return JSONResponse(
                content = {
                    'message': 'file too large (MAX: 10 MB)',
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'data': answer
                },
                status_code = HTTPStatus.BAD_REQUEST
            )

        # check the content type (MIME type)
        content_type = file.content_type
        if content_type not in ["image/jpeg", "image/png", "image/gif"]:
            return JSONResponse(
                content = {
                    'message': 'invalid file type',
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'data': answer
                },
                status_code = HTTPStatus.BAD_REQUEST
            )
            
        # Answer
        answer: str = self._IMAGE_RECOG_SERVICE.predict_image(file)
        return JSONResponse(
            content = {
                'message': 'Predict Success',
                'status_code': HTTPStatus.OK,
                'data': answer
            },
            status_code = HTTPStatus.OK
        )
