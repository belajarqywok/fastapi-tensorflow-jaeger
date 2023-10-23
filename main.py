import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from src.configurations.databases.postgresql import Session
from src.routes import (
    ml_routes,
    user_routes,
    main_routes
)

load_dotenv()

# Database Connection
DATABASE: Session = Session()

REST = FastAPI(
    title = "NLP service",
    version = os.getenv("VERSION")
)

# CORS Middleware
REST.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,
)

# Include predict route group
REST.include_router(
    router = ml_routes.route,
    prefix = f'/{os.getenv("VERSION")}/vertx',
    tags = ["Predict"],
)

# Include user route group
REST.include_router(
    router = user_routes.route,
    prefix = f'/{os.getenv("VERSION")}/auth',
    tags = ["User"],
)

# Include main route group
REST.include_router(
    router = main_routes.route,
    prefix = f'',
    tags = ["Main"],
)

@REST.on_event("shutdown")
async def shutdown_event():
    # Database Connection Close
    DATABASE.close()
    