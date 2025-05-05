"""
FastAPI 应用入口。
"""

from fastapi import FastAPI, Request
from src.api.math import router as math_router

app: FastAPI = FastAPI()
app.include_router(math_router)

@app.post("/_pact/provider_states")
async def provider_states(request: Request) -> dict:
    """
    Pact Provider State Handler
    用于契约测试时根据 state 字段准备后端状态。
    """
    body = await request.json()
    state = body.get("state")
    if state == "加法服务可用":
        # 这里可以做任何你需要的准备动作，比如重置数据、初始化依赖等
        print("Provider State: 加法服务可用 -> 已准备好")
        # 你可以在这里设置全局变量、清空缓存、插入测试数据等
    return {} 