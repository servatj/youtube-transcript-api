# app/__init__.py
"""
This is the main package for the FastAPI application.
"""

from fastapi import FastAPI
from app.api.endpoints import transcript, analyze

# Initialize the FastAPI app
app = FastAPI(title="YouTube Transcript API")

# Include routers for different endpoints
app.include_router(transcript.router, prefix="/transcript", tags=["Transcript"])
app.include_router(analyze.router, prefix="/analyze", tags=["Analyze"])