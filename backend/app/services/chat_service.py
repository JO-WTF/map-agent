from app.agent.graph import SupervisorGraph


class ChatService:
    def __init__(self) -> None:
        self.graph = SupervisorGraph()

    def chat(self, session_id: str, message: str, file_ids: list[str]) -> dict:
        return self.graph.plan(session_id, message, file_ids)
