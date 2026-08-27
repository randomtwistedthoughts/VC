from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgentState:
  targetL str = ""
  messages: list[dict[str, Any]] = field(default_factory=list)
  evidence: list[Any] = field(default_factory=list)
  findings: list[Any} = field(default_factory=list)
  step: int = 0
  finished: bool = False
  
