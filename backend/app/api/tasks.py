from fastapi import APIRouter, HTTPException
from app.container import task_store
from app.schemas.task import TaskStatusResponse, TaskResultResponse

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("/{task_id}", response_model=TaskStatusResponse)
def get_task(task_id: str) -> TaskStatusResponse:
    try:
        t = task_store.get(task_id)
    except KeyError as exc:
        raise HTTPException(404, "task not found") from exc
    return TaskStatusResponse(task_id=t['task_id'], status=t['status'], progress=t['progress'], current_step=t['current_step'], updated_at=t['updated_at'])


@router.get("/{task_id}/result", response_model=TaskResultResponse)
def get_task_result(task_id: str) -> TaskResultResponse:
    t = task_store.get(task_id)
    return TaskResultResponse(task_id=t['task_id'], result=t['result'])
