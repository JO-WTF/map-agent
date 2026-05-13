from fastapi import APIRouter
from app.container import runtime_service

router = APIRouter(prefix="/api/tools", tags=["tools"])


@router.get("")
def list_tools() -> list[dict]:
    return [{"name": t.name, "description": t.description, "risk_level": t.risk_level, "enabled": t.enabled} for t in runtime_service.tool_registry.list()]
