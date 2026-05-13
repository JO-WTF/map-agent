from datetime import datetime
from pydantic import BaseModel


class LogItem(BaseModel):
    step: str
    message: str
    status: str


class Timestamped(BaseModel):
    created_at: datetime
    updated_at: datetime
