import json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.container import chat_service, task_store, runtime_service

router = APIRouter(prefix="/api/chat", tags=["chat"])


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


@router.post("")
def chat(req: ChatRequest) -> StreamingResponse:
    def event_stream():
        plan = chat_service.chat(req.session_id, req.message, req.file_ids)
        yield _sse("message", {"token": "正在分析你的问题..."})
        for step in plan.get("steps", []):
            yield _sse("agent_step", {"step": step})

        if plan["need_user_input"]:
            yield _sse("need_user_input", {"message": plan["agent_message"], "fields": ["file_ids"]})
            yield _sse("done", {"status": "waiting_user_input"})
            return

        task = task_store.create(plan["skill_name"], req.model_dump())
        yield _sse("task_status", {"task_id": task["task_id"], "status": "queued", "progress": 0})
        yield _sse("tool_call", {"tool": "warehouse_customer_allocation_skill", "status": "start"})
        runtime_service.execute_skill(task)
        yield _sse("task_status", {"task_id": task["task_id"], "status": task["status"], "progress": task["progress"]})
        yield _sse("task_log", {"message": "skill execution finished", "status": "success"})
        yield _sse(
            "result_ref",
            {
                "task_id": task["task_id"],
                "result_endpoint": f"/api/tasks/{task['task_id']}/result",
                "map": True,
                "charts": True,
                "tables": True,
            },
        )
        yield _sse("done", {"status": "success"})

    return StreamingResponse(event_stream(), media_type="text/event-stream")
