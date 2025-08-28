# core/middleware.py
import time, logging
from fastapi import Request

logger = logging.getLogger("student-management")

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = (time.time() - start_time) * 1000
    logger.info("%s %s - %sms", request.method, request.url.path, f"{duration:.2f}")
    return response

