from fastapi.testclient import TestClient
from app.main import app


def test_chat_sse_task_and_result_flow() -> None:
    client = TestClient(app)
    with client.stream("POST", "/api/chat", json={"session_id": "s1", "message": "帮我分析这些客户应该分配到哪个仓库", "file_ids": ["file_001"]}) as resp:
        assert resp.status_code == 200
        assert "text/event-stream" in resp.headers["content-type"]
        body = "".join(resp.iter_text())

    assert "event: task_status" in body
    assert "event: result_ref" in body

    # extract task_id from stream payload quickly
    import re
    m = re.search(r'"task_id": "(task_[a-z0-9]+)"', body)
    assert m
    task_id = m.group(1)

    status = client.get(f"/api/tasks/{task_id}")
    assert status.status_code == 200
    result = client.get(f"/api/tasks/{task_id}/result")
    assert "map_data" in result.json()["result"]
