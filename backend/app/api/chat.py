import json
from datetime import datetime, UTC
from uuid import uuid4
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.container import chat_service, task_store, runtime_service

router = APIRouter(prefix="/api/chat", tags=["chat"])


def sse_event(event_type: str, run_id: str, session_id: str, data: dict) -> str:
    payload = {
        "event_id": f"evt_{uuid4().hex[:8]}",
        "type": event_type,
        "timestamp": datetime.now(UTC).isoformat(),
        "run_id": run_id,
        "session_id": session_id,
        "data": data,
    }
    return f"event: {event_type}\ndata: {json.dumps(payload, ensure_ascii=False)}\n\n"


@router.post("/stream")
def chat_stream(req: ChatRequest) -> StreamingResponse:
    def event_generator():
        run_id = f"run_{uuid4().hex[:8]}"
        plan = chat_service.chat(req.session_id, req.message, req.file_ids)

        yield sse_event("run.started", run_id, req.session_id, {"run_id": run_id, "message": "开始处理请求"})
        yield sse_event("agent.thought", run_id, req.session_id, {"content": "我将先确认输入数据，再选择最合适的物流分配 Skill。"})
        yield sse_event("message.delta", run_id, req.session_id, {"content": plan["agent_message"]})
        yield sse_event(
            "skill.selected",
            run_id,
            req.session_id,
            {"skill_name": plan["skill_name"], "reason": "用户请求客户到仓库分配并统计时效"},
        )

        if plan["need_user_input"]:
            yield sse_event(
                "input.required",
                run_id,
                req.session_id,
                {
                    "question": "请先上传客户文件后继续分析。",
                    "required_fields": [{"name": "file_ids", "label": "客户文件", "options": []}],
                },
            )
            yield sse_event("run.finished", run_id, req.session_id, {"run_id": run_id, "status": "waiting_user_input"})
            return

        task = task_store.create(plan["skill_name"], req.model_dump())
        yield sse_event("task.created", run_id, req.session_id, {"task_id": task["task_id"], "status": "queued"})

        yield sse_event("tool.started", run_id, req.session_id, {"tool_call_id": "tool_call_001", "tool_name": "get_warehouses", "display_name": "获取仓库信息", "input_preview": {"source": "remote_api"}})
        runtime_service.execute_skill(task)
        yield sse_event("tool.finished", run_id, req.session_id, {"tool_call_id": "tool_call_001", "tool_name": "get_warehouses", "status": "success", "duration_ms": 10, "output_preview": {"warehouse_count": 2}})

        yield sse_event("task.progress", run_id, req.session_id, {"task_id": task["task_id"], "progress": 100, "current_step": "执行完成"})
        yield sse_event("result.ready", run_id, req.session_id, {"task_id": task["task_id"], "result_id": f"result_{task['task_id']}", "result_url": f"/api/tasks/{task['task_id']}/result", "has_map": True, "has_charts": True, "has_tables": True})
        yield sse_event("run.finished", run_id, req.session_id, {"run_id": run_id, "status": "success"})

    return StreamingResponse(event_generator(), media_type="text/event-stream", headers={"Cache-Control": "no-cache", "Connection": "keep-alive", "X-Accel-Buffering": "no"})
