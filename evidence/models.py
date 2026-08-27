from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Evidence:
    tool: str
    target: str
    data: Any
    timestamp: datetime = field(default_factory=datetime.now)
