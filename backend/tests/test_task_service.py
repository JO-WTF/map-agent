from app.services.task_service import TaskService
from app.schemas.task import TaskRequest


def test_run_task_returns_completed_payload() -> None:
    svc = TaskService()
    result = svc.run_task(TaskRequest(query="run logistics allocation"))
    assert result.status == "completed"
    assert len(result.table_data) > 0
    assert "connections" in result.map_data
