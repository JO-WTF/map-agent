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
            "events": [],
        }
        self.tasks[task_id] = row
        self.add_event(task_id, "task.created", {"task_id": task_id, "status": "queued", "progress": 0})
        return row

    def get(self, task_id: str) -> dict:
        return self.tasks[task_id]

    def update(self, task_id: str, **kwargs) -> dict:
        task = self.tasks[task_id]
        task.update(kwargs)
        task["updated_at"] = datetime.now(UTC)
        return task

    def add_event(self, task_id: str, event_type: str, data: dict) -> None:
        task = self.tasks[task_id]
        task["events"].append(
            {
                "seq": len(task["events"]) + 1,
                "type": event_type,
                "timestamp": datetime.now(UTC).isoformat(),
                "data": data,
            }
        )

    def get_events_after(self, task_id: str, after_seq: int) -> list[dict]:
        task = self.tasks[task_id]
        return [e for e in task["events"] if e["seq"] > after_seq]
