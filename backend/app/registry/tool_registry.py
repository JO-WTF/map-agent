from app.registry.schemas import ToolMeta


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolMeta] = {}

    def register(self, meta: ToolMeta) -> None:
        self._tools[meta.name] = meta

    def list(self) -> list[ToolMeta]:
        return [t for t in self._tools.values() if t.enabled]

    def get(self, name: str) -> ToolMeta:
        return self._tools[name]
