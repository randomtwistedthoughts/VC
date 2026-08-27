
from .models import Evidence


class EvidenceStore:
    def __init__(self):
        self._items: list[Evidence] = []

    def add(self, evidence: Evidence) -> None:
        self._items.append(evidence)

    def all(self) -> list[Evidence]:
        return self._items

    def count(self) -> int:
        return len(self._items)
