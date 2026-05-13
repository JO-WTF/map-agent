from datetime import datetime, UTC
from uuid import uuid4
from app.tasks.task_status import TaskStatus


class TaskStore:
    def __init__(self) -> None:
        self.tasks: dict[str, dict] = {}

    def create(self, skill_name: str, payload: dict) -> dict:
        task_id = f"task_{uuid4().hex[:8]}"
        row = {
            "task_id": task_id,
            "status": TaskStatus.queued,
            "progress": 0,
            "current_step": "queued",
            "skill_name": skill_name,
            "input": payload,
            "result": None,
            "updated_at": datetime.now(UTC),
        }
        self.tasks[task_id] = row
        return row

    def get(self, task_id: str) -> dict:
        return self.tasks[task_id]
