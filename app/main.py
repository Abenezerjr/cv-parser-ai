from fastapi import FastAPI
from app.api.routers import parse

app = FastAPI(title="CV Parser API")

app.include_router(parse.router, prefix="/api")
