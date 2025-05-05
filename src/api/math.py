"""
数学运算相关 API 路由。
""" 
from fastapi import APIRouter, HTTPException, status
from src.models.math import MathRequest, MathResponse

router: APIRouter = APIRouter(prefix="/api/math", tags=["math"])

@router.post("/add", response_model=MathResponse, summary="加法运算")
def add_numbers(request: MathRequest) -> MathResponse:
    """
    执行加法运算。
    
    Args:
        request (MathRequest): 包含两个操作数的请求体。
    
    Returns:
        MathResponse: 运算结果。
    """
    try:
        result: float = request.a + request.b
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"加法运算失败: {exc}"
        )
    return MathResponse(result=result) 