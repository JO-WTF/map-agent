from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.container import chat_service, task_store, runtime_service

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    plan = chat_service.chat(req.session_id, req.message, req.file_ids)
    if plan["need_user_input"]:
        return ChatResponse(message=plan["agent_message"], need_user_input=True)
    task = task_store.create(plan["skill_name"], req.model_dump())
    runtime_service.execute_skill(task)
    return ChatResponse(message=plan["agent_message"], task_id=task["task_id"], need_user_input=False)
