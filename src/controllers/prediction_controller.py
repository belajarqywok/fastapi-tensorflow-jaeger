from http import HTTPStatus
from fastapi.responses import JSONResponse
from src.services.prediction_service import prediction_service

# Prediction Controller
class prediction_controller():
    # Prediction Service
    _SERVICE = prediction_service()

    # Question Predict
    def question_predict(self, question: str) -> JSONResponse:
        # Answer
        answer: str = self._SERVICE.predict_question(
            question = question
        )

        return JSONResponse(
            content = {
                'message': 'Predict Success',
                'status_code': HTTPStatus.OK,
                'data': answer
            },
            status_code = HTTPStatus.OK
        )
