"""
数学运算请求与响应模型。
"""
from pydantic import BaseModel, Field

class MathRequest(BaseModel):
    """
    请求体模型：包含两个操作数。
    """
    a: float = Field(..., description="第一个操作数")
    b: float = Field(..., description="第二个操作数")

class MathResponse(BaseModel):
    """
    响应体模型：返回运算结果。
    """
    result: float = Field(..., description="运算结果") 