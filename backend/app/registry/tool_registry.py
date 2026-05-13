from typing import Callable


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Callable] = {}

    def register(self, name: str, fn: Callable) -> None:
        self._tools[name] = fn

    def get(self, name: str) -> Callable:
        if name not in self._tools:
            raise ValueError(f"tool not found: {name}")
        return self._tools[name]

    def list(self) -> list[str]:
        return sorted(self._tools.keys())
