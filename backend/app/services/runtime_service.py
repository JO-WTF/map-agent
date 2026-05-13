from datetime import datetime, UTC
from app.registry.skill_registry import SkillRegistry
from app.registry.tool_registry import ToolRegistry
from app.registry.schemas import SkillMeta, ToolMeta
from app.skills.warehouse_allocation.skill import run as warehouse_run
from app.tools.remote_api.warehouse_api import get_warehouses
from app.tools.remote_api.customer_api import get_customers


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

    def execute_skill(self, task: dict) -> dict:
        meta = self.skill_registry.get(task['skill_name'])
        task['status'] = 'running'
        task['progress'] = 50
        task['current_step'] = 'running skill'
        task['updated_at'] = datetime.now(UTC)
        result = meta.handler(task['task_id'], task['input'])
        task['status'] = 'success'
        task['progress'] = 100
        task['current_step'] = 'done'
        task['result'] = result
        task['updated_at'] = datetime.now(UTC)
        return task
