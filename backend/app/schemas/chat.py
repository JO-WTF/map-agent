from pydantic import BaseModel


class ChatContext(BaseModel):
    current_skill: str | None = None
    current_task_id: str | None = None


class ChatRequest(BaseModel):
    session_id: str
    message: str
    file_ids: list[str] = []
    context: ChatContext = ChatContext()
