from enum import StrEnum


class TaskStatus(StrEnum):
    queued = "queued"
    running = "running"
    waiting_user_input = "waiting_user_input"
    success = "success"
    failed = "failed"
    cancelled = "cancelled"
