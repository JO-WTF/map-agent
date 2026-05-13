from app.agent.state import AgentState
from app.agent.supervisor import select_skill


class SupervisorGraph:
    def plan(self, session_id: str, message: str, file_ids: list[str]) -> dict:
        state = AgentState(session_id=session_id, message=message, file_ids=file_ids)
        skill = select_skill(state)
        need_user_input = len(file_ids) == 0 and "这些客户" in message
        return {
            "skill_name": skill,
            "need_user_input": need_user_input,
            "agent_message": "我会使用仓库客户分配 Skill 进行分析。" if not need_user_input else "请先上传客户文件。",
        }
