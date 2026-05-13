import json
import time
from fastapi.testclient import TestClient
from app.main import app


def test_chat_stream_and_task_events_flow() -> None:
    client = TestClient(app)
    with client.stream("POST", "/api/chat/stream", json={
        "session_id": "session_001",
        "message": "帮我分析上传的客户文件，分配到最近仓库并统计时效",
        "file_ids": ["file_001"],
        "context": {"current_skill": None, "current_task_id": None},
    }) as resp:
        assert resp.status_code == 200
        body = "".join(resp.iter_text())

    assert "event: task.created" in body
    result_line = [line for line in body.splitlines() if line.startswith("data: ") and '"type": "task.created"' in line][0]
    payload = json.loads(result_line.removeprefix("data: "))
    task_id = payload["data"]["task_id"]

    # allow background worker to run
    time.sleep(0.3)

    with client.stream("GET", f"/api/tasks/{task_id}/events") as resp2:
        assert resp2.status_code == 200
        events_body = "".join(resp2.iter_text())

    assert "event: task.progress" in events_body
    assert "event: result.ready" in events_body

    result = client.get(f"/api/tasks/{task_id}/result")
    assert result.status_code == 200
    assert "map_data" in result.json()["result"]
