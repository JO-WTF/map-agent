import time
from datetime import datetime, UTC
from app.registry.skill_registry import SkillRegistry
from app.registry.tool_registry import ToolRegistry
from app.registry.schemas import SkillMeta, ToolMeta
from app.skills.warehouse_allocation.skill import run as warehouse_run
from app.tools.remote_api.warehouse_api import get_warehouses
from app.tools.remote_api.customer_api import get_customers


def normalize_agent_event(event_type: str, task_id: str, data: dict) -> dict:
    return {
        "type": event_type,
        "timestamp": datetime.now(UTC).isoformat(),
        "task_id": task_id,
        "data": data,
    }


class RuntimeService:
    def __init__(self) -> None:
        self.skill_registry = SkillRegistry()
        self.tool_registry = ToolRegistry()
        self._bootstrap()

    def _bootstrap(self) -> None:
        self.skill_registry.register(SkillMeta(
            name="warehouse_customer_allocation_skill",
            description="仓库客户分配与配送时效统计",
            version="1.0.0",
            input_schema={},
            output_schema={},
            handler=warehouse_run,
        ))
        self.tool_registry.register(ToolMeta(name="get_warehouses", description="fetch warehouses", handler=get_warehouses))
        self.tool_registry.register(ToolMeta(name="get_customers", description="fetch customers", handler=get_customers))

    def execute_skill(self, task: dict, on_event=None) -> dict:
        meta = self.skill_registry.get(task['skill_name'])
        task_id = task["task_id"]
        task['status'] = 'running'
        task['progress'] = 10
        task['current_step'] = 'start skill'
        task['updated_at'] = datetime.now(UTC)
        if on_event:
            on_event(normalize_agent_event("task.progress", task_id, {"progress": 10, "current_step": task['current_step']}))

        tool_call_id = f"tool_{int(time.time()*1000)}"
        started_at = time.perf_counter()
        if on_event:
            on_event(normalize_agent_event("tool.started", task_id, {"tool_call_id": tool_call_id, "tool_name": meta.name, "input_preview": task['input']}))

        result = meta.handler(task['task_id'], task['input'])

        duration_ms = int((time.perf_counter() - started_at) * 1000)
        if on_event:
            on_event(normalize_agent_event("tool.finished", task_id, {"tool_call_id": tool_call_id, "tool_name": meta.name, "status": "success", "duration_ms": duration_ms, "output_preview": {"keys": list(result.keys())}}))

        task['status'] = 'success'
        task['progress'] = 100
        task['current_step'] = 'done'
        task['result'] = result
        task['updated_at'] = datetime.now(UTC)
        if on_event:
            on_event(normalize_agent_event("task.progress", task_id, {"progress": 100, "current_step": "done"}))
            on_event(normalize_agent_event("result.ready", task_id, {"task_id": task_id, "result_url": f"/api/tasks/{task_id}/result"}))
        return task
