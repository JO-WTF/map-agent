from dataclasses import dataclass


@dataclass
class AgentState:
    session_id: str
    message: str
    file_ids: list[str]
