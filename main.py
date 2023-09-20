import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from src.configurations.databases.postgresql import Session
from src.routes import (
    user_routes,
    predict_routes
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
    router = predict_routes.route,
    prefix = f'/{os.getenv("VERSION")}',
    tags = ["Predict"],
)

# Include user route group
REST.include_router(
    router = user_routes.route,
    prefix = f'/{os.getenv("VERSION")}',
    tags = ["User"],
)

@REST.on_event("shutdown")
async def shutdown_event():
    # Database Connection Close
    DATABASE.close()