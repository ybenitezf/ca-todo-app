from dataclasses import dataclass
from datetime import date


@dataclass
class TodoItem:
    owner: str
    title: str
    description: str
    is_done: bool = False
    due_date: date | None = None
