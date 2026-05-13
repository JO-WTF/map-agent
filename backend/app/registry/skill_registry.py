from app.registry.schemas import SkillMeta


class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, SkillMeta] = {}

    def register(self, meta: SkillMeta) -> None:
        self._skills[meta.name] = meta

    def list(self) -> list[SkillMeta]:
        return [s for s in self._skills.values() if s.enabled]

    def get(self, name: str) -> SkillMeta:
        return self._skills[name]
