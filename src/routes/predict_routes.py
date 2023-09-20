from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from src.configurations.security.jwt_utils import auth_utilities
from src.controllers.prediction_controller import prediction_controller

# Api Router
route = APIRouter()

# Auth Utilities
AUTH_UTILS = auth_utilities()

# Prediction Controller
__CONTROLLER = prediction_controller()

@route.get('/predict')
async def prediction_route(
    question: str,
    _ = Depends(AUTH_UTILS.authorization)
) -> JSONResponse:
    # Question Predict
    return __CONTROLLER.question_predict(
        question = question
    )