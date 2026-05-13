from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    message: str
    file_ids: list[str] = []


class ChatEvent(BaseModel):
    event: str
    data: dict
