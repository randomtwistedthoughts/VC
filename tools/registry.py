from collections.abc import Callable 
from typing import Any

class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, function: Callable[..., Any]) -> None:
        self._tools[name] = function

    def get(self, name:str) -> Callable[..., Any]:
      if name not in self._tools:
        raise KeyError(f"Tool not found: {name}")

      return self._tools[name]

      def list_tools(self) -> list[str]:
        return list(self._tools.keys())

      def execute(self, name: str, **kwargs: Any) -> Any:
        tool = self.get(name)
        return tool(**kwargs)
       

