# app/api/__init__.py
"""
This module initializes the API package.
"""

from fastapi import APIRouter
from app.api.endpoints.transcript import router as transcript_router
from app.api.endpoints.analyze import router as analyze_router
from app.api.endpoints.system import router as health_router

# Initialize the main API router
api_router = APIRouter()

# Include individual routers
api_router.include_router(transcript_router, prefix="/transcript", tags=["Transcript"])
api_router.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])
api_router.include_router(health_router, prefix="/system", tags=["System"])