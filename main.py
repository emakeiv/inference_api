from fastapi import FastAPI
from app.api.endpoints import sections
from app.api.security.auth import AuthorizeRequestMiddleware
from fastapi.middleware.cors import CORSMiddleware

def create_server():
    server = FastAPI(debug=True)
    server.add_middleware(AuthorizeRequestMiddleware)
    server.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    server.include_router(sections.router)

    return server

server = create_server()