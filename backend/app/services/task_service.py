from uuid import uuid4
from app.registry.tool_registry import ToolRegistry
from app.registry.skill_registry import SkillRegistry
from app.skills.warehouse_customer_allocation_skill import warehouse_customer_allocation_skill
from app.schemas.task import TaskRequest, TaskResponse
from app.tools import logistics_tools as tools


class TaskService:
    def __init__(self) -> None:
        self.tool_registry = ToolRegistry()
        self.skill_registry = SkillRegistry()
        self._register_defaults()

    def _register_defaults(self) -> None:
        self.tool_registry.register("get_warehouses", tools.get_warehouses)
        self.tool_registry.register("get_customers", tools.get_customers)
        self.tool_registry.register("calculate_distance_matrix", tools.calculate_distance_matrix)
        self.tool_registry.register("assign_nearest_warehouse", tools.assign_nearest_warehouse)
        self.tool_registry.register("calculate_delivery_sla", tools.calculate_delivery_sla)
        self.tool_registry.register("aggregate_warehouse_sla_stats", tools.aggregate_warehouse_sla_stats)
        self.tool_registry.register("generate_map_data", tools.generate_map_data)
        self.tool_registry.register("generate_chart_data", tools.generate_chart_data)
        self.skill_registry.register("warehouse_customer_allocation_skill", warehouse_customer_allocation_skill)

    def list_tools(self) -> list[str]:
        return self.tool_registry.list()

    def list_skills(self) -> list[str]:
        return self.skill_registry.list()

    def run_task(self, payload: TaskRequest) -> TaskResponse:
        selected_skill = payload.use_skill or "warehouse_customer_allocation_skill"
        if selected_skill not in self.skill_registry.list():
            raise ValueError(f"unknown skill: {selected_skill}")
        result = self.skill_registry.get(selected_skill)()
        return TaskResponse(
            task_id=str(uuid4()),
            status="completed",
            map_data=result["map_data"],
            chart_data=result["chart_data"],
            table_data=result["table_data"],
            logs=result["logs"],
        )
