from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from src.controllers.auth_controllers import auth_controllers
from src.schemas.user_request_schema import (
    RegisterRequestSchema,
    RefreshRequestSchema, 
    LoginRequestSchema
)

# Route
route = APIRouter()

# Controller
__CONTROLLER = auth_controllers()

# Register Path
@route.post(path = '/register', tags = ['auth'])
async def register_route(
    payload: RegisterRequestSchema = Body(...)
) -> JSONResponse:
    # Register Controller
    return __CONTROLLER.register(payload = payload)


# Login Path
@route.post(path = '/login', tags = ['auth'])
async def login_route(
    payload: LoginRequestSchema = Body(...)
) -> JSONResponse :
    # Login Controller
    return __CONTROLLER.login(payload = payload)


# Refresh Token Path
@route.post(path = '/refresh', tags = ['auth'])
async def refresh_token_route(
    payload: RefreshRequestSchema = Body(...)
) -> JSONResponse :
    # Refresh Token Controller
    return __CONTROLLER.refresh_token(payload = payload)