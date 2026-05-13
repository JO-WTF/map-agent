from typing import Callable


class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, Callable] = {}

    def register(self, name: str, fn: Callable) -> None:
        self._skills[name] = fn

    def get(self, name: str) -> Callable:
        if name not in self._skills:
            raise ValueError(f"skill not found: {name}")
        return self._skills[name]

    def list(self) -> list[str]:
        return sorted(self._skills.keys())
