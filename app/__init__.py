# app/__init__.py
"""
This is the main package for the FastAPI application.
"""

from fastapi import FastAPI
from app.api import api_router

# Initialize the FastAPI app
app = FastAPI(title="YouTube Transcript API")

# Include routers for different endpoints
app.include_router(api_router)
