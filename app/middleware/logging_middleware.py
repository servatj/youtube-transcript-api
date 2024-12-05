# app/middleware/logging_middleware.py
import uuid
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("fastapi")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        request.state.correlation_id = correlation_id

        logger.info(f"[{correlation_id}] Incoming {request.method} {request.url}")

        response = await call_next(request)

        # Log the outgoing response
        logger.info(f"[{correlation_id}] Response status: {response.status_code}")

        response.headers["X-Correlation-ID"] = correlation_id
        return response
