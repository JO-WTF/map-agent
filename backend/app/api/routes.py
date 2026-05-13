from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskRequest, TaskResponse
from app.services.task_service import TaskService

router = APIRouter(prefix="/api")
service = TaskService()


@router.get("/tools")
def list_tools() -> dict:
    return {"tools": service.list_tools()}


@router.get("/skills")
def list_skills() -> dict:
    return {"skills": service.list_skills()}


@router.post("/tasks", response_model=TaskResponse)
def create_task(payload: TaskRequest) -> TaskResponse:
    try:
        return service.run_task(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
