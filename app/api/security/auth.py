import time
from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from starlette.middleware.base import BaseHTTPMiddleware

class AuthorizeRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        response.headers['X-Process-Time'] = str(process_time)
        return response