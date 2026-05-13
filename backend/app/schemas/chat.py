from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    message: str
    file_ids: list[str] = []


class ChatResponse(BaseModel):
    message: str
    task_id: str | None = None
    need_user_input: bool
