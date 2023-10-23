from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.controllers.main_controllers import main_controllers

# Route
route = APIRouter()

# Controller
__CONTROLLER = main_controllers()


# Main Path
@route.get(path = '/', tags = ['main'])
async def main_route() -> JSONResponse:
    # Main Controller
    return __CONTROLLER.main()


# Liveness Check Path
@route.get(path = '/liveness_check', tags = ['main'])
async def liveness_check_route() -> JSONResponse:
    # Liveness Check Controller
    return __CONTROLLER.liveness_check()


# Readiness Check Path
@route.get(path = '/readiness_check', tags = ['main'])
async def readiness_check_route() -> JSONResponse:
    # Readiness Check Controller
    return __CONTROLLER.readiness_check()
