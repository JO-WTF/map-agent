from app.agent.state import AgentState


def select_skill(state: AgentState) -> str:
    if "分配" in state.message or "仓库" in state.message:
        return "warehouse_customer_allocation_skill"
    return "warehouse_customer_allocation_skill"
