# app/middleware/request_counter.py
import logging
from fastapi import FastAPI, Request

logger = logging.getLogger("request_counter")

def register_request_counter(app: FastAPI) -> None:
    app.state.request_count = 0  # per-process counter

    @app.middleware("http")
    async def count_requests(request: Request, call_next):
        app.state.request_count += 1
        logger.info("Total requests so far: %s", app.state.request_count)
        response = await call_next(request)
        return response
