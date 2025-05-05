"""
加法 API 单元测试。
"""
import pytest
from typing import TYPE_CHECKING
from fastapi.testclient import TestClient
from src.main import app

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture

test_client: TestClient = TestClient(app)

def test_add_api() -> None:
    """
    测试加法 API 的正常返回。
    """
    response = test_client.post("/api/math/add", json={"a": 2.5, "b": 3.5})
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert data["result"] == pytest.approx(6.0) 