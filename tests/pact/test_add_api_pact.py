"""
加法 API Pact 合约测试。
"""
import pytest
from pact import Consumer, Provider
from requests import post

PACT_MOCK_HOST = "localhost"
PACT_MOCK_PORT = 1234

@pytest.fixture(scope="module")
def pact():
    pact = Consumer("math-api-consumer").has_pact_with(
        Provider("math-api-provider"),
        host_name=PACT_MOCK_HOST,
        port=PACT_MOCK_PORT,
    )
    pact.start_service()
    yield pact
    pact.stop_service()

def test_add_api_contract(pact) -> None:
    """
    验证加法 API 的 Pact 合约。
    """
    expected = {"result": 6.0}
    (pact
     .given("加法服务可用")
     .upon_receiving("一个加法请求")
     .with_request(
         method="POST",
         path="/api/math/add",
         headers={"Content-Type": "application/json"},
         body={"a": 2.5, "b": 3.5}
     )
     .will_respond_with(
         status=200,
         headers={"Content-Type": "application/json"},
         body=expected
     ))
    with pact:
        result = post(
            f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}/api/math/add",
            json={"a": 2.5, "b": 3.5}
        )
        assert result.status_code == 200
        assert result.json() == expected 