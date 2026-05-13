from dataclasses import dataclass
from typing import Callable


@dataclass
class SkillMeta:
    name: str
    description: str
    version: str
    input_schema: dict
    output_schema: dict
    visible_to_agent: bool = True
    requires_confirmation: bool = False
    timeout_seconds: int = 600
    enabled: bool = True
    handler: Callable | None = None


@dataclass
class ToolMeta:
    name: str
    description: str
    risk_level: str = "low"
    visible_to_agent: bool = True
    timeout_seconds: int = 60
    enabled: bool = True
    handler: Callable | None = None
