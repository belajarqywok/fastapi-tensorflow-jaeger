from http import HTTPStatus
from fastapi.responses import JSONResponse
from src.services.ml_services.nlp_service import nlp_service

# NLP Controller
class nlp_controller():
    # NLP Service
    _NLP_SERVICE = nlp_service()

    # Question Predict
    def question_predict(self, question: str) -> JSONResponse:
        # Answer
        answer: str = self._NLP_SERVICE.predict_question(
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
