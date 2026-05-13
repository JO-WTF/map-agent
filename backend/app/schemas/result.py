from pydantic import BaseModel
from app.schemas.common import LogItem


class ResultBundle(BaseModel):
    summary: dict
    map_data: dict
    charts: dict
    tables: dict
    files: dict
    logs: list[LogItem]
