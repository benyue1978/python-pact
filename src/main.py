"""
FastAPI 应用入口。
"""

from fastapi import FastAPI
from src.api.math import router as math_router

app: FastAPI = FastAPI()
app.include_router(math_router) 