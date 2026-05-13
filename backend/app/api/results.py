from fastapi import APIRouter
from app.container import task_store

router = APIRouter(prefix="/api/results", tags=["results"])


@router.get("/{task_id}")
def get_result_bundle(task_id: str) -> dict:
    return task_store.get(task_id).get("result") or {}
