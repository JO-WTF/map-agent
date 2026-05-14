from fastapi import APIRouter
from app.container import runtime_service

router = APIRouter(prefix="/api/skills", tags=["skills"])


@router.get("")
def list_skills() -> list[dict]:
    return [{"name": s.name, "description": s.description, "version": s.version, "enabled": s.enabled} for s in runtime_service.skill_registry.list()]
