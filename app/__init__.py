# app/__init__.py
"""
This is the main package for the FastAPI application.
"""

from dotenv import load_dotenv
import os

# Load environment variables first
load_dotenv()

from fastapi import FastAPI
from app.api import api_router
from app.middleware.logging_middleware import LoggingMiddleware

# Initialize the FastAPI app
app = FastAPI(title="YouTube Transcript API")

# Include routers for different endpoints
app.include_router(api_router)
app.add_middleware(LoggingMiddleware)
