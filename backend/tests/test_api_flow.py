import json
from fastapi.testclient import TestClient
from app.main import app


def test_chat_stream_sse_protocol_and_result_flow() -> None:
    client = TestClient(app)
    with client.stream("POST", "/api/chat/stream", json={
        "session_id": "session_001",
        "message": "帮我分析上传的客户文件，分配到最近仓库并统计时效",
        "file_ids": ["file_001"],
        "context": {"current_skill": None, "current_task_id": None},
    }) as resp:
        assert resp.status_code == 200
        assert "text/event-stream" in resp.headers["content-type"]
        body = "".join(resp.iter_text())

    for expected in ["run.started", "message.delta", "skill.selected", "tool.started", "tool.finished", "task.progress", "result.ready", "run.finished"]:
        assert f"event: {expected}" in body

    result_line = [line for line in body.splitlines() if line.startswith("data: ") and '"type": "result.ready"' in line][0]
    payload = json.loads(result_line.removeprefix("data: "))
    task_id = payload["data"]["task_id"]

    result = client.get(f"/api/tasks/{task_id}/result")
    assert result.status_code == 200
    assert "map_data" in result.json()["result"]
