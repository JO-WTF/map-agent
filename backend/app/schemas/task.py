from datetime import datetime
from pydantic import BaseModel, Field
from app.schemas.result import ResultBundle


class TaskCreateRequest(BaseModel):
    session_id: str
    message: str
    file_ids: list[str] = []


class TaskStatusResponse(BaseModel):
    task_id: str
    status: str
    progress: int = Field(ge=0, le=100)
    current_step: str
    updated_at: datetime


class TaskResultResponse(BaseModel):
    task_id: str
    result: ResultBundle
