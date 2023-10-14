from fastapi import File, UploadFile
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from src.configurations.security.jwt_utils import auth_utilities
from src.controllers.ml_controllers import nlp_controller, image_recog_controller

# Api Router
route = APIRouter()

# Auth Utilities
__AUTH_UTILS = auth_utilities()

# ML Controllers
__NLP_CONTROLLER = nlp_controller.nlp_controller()
__IMAGE_RECOG_CONTROLLER = image_recog_controller.image_recog_controller()


# Word Prediction Route
@route.get('/word_predict')
async def word_prediction_route(
    question: str,
    _ = Depends(__AUTH_UTILS.authorization)
) -> JSONResponse:
    # Question Predict
    return __NLP_CONTROLLER.question_predict(question)


# Image Prediction Route
@route.post('/image_predict')
async def image_prediction_route(
    file: UploadFile = File(...),
    _ = Depends(__AUTH_UTILS.authorization)
) -> JSONResponse:
    # Question Predict
    return await __IMAGE_RECOG_CONTROLLER.image_predict(file)
