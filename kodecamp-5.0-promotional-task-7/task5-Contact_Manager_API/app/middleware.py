import logging
from datetime import datetime

from fastapi import Request

logger = logging.getLogger("uvicorn.access")

async def ip_logger(request: Request, call_next):
    xff = request.headers.get("x-forwarded-for")
    ip = xff.split(",")[0].strip() if xff else (request.client.host if request.client else "unknown")
    now = datetime.utcnow().isoformat()
    logger.info(f"[{now}] Request from IP: {ip} {request.method} {request.url}")
    response = await call_next(request)
    return response