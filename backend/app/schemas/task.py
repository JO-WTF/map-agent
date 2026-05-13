from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    query: str = Field(..., min_length=3)
    use_skill: str | None = None


class TaskResponse(BaseModel):
    task_id: str
    status: str
    map_data: dict
    chart_data: dict
    table_data: list[dict]
    logs: list[str]
