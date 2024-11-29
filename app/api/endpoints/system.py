from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os

router = APIRouter()

@router.get("/health")
async def health_check():
  """
  Health check endpoint to provide basic metrics.
  """
  metrics = {
    "status": "healthy",
    "uptime": os.popen('uptime').read().strip(),
    "disk_usage": os.popen('df -h /').read().strip(),
    "memory_usage": os.popen('free -h').read().strip()
  }
  return JSONResponse(content=metrics)