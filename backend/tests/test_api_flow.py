from fastapi.testclient import TestClient
from app.main import app


def test_chat_task_and_result_flow() -> None:
    client = TestClient(app)
    chat = client.post('/api/chat', json={"session_id": "s1", "message": "帮我分析这些客户应该分配到哪个仓库", "file_ids": ["file_001"]})
    assert chat.status_code == 200
    task_id = chat.json()["task_id"]
    status = client.get(f'/api/tasks/{task_id}')
    assert status.status_code == 200
    assert status.json()["status"] == "success"
    result = client.get(f'/api/tasks/{task_id}/result')
    assert "map_data" in result.json()["result"]
