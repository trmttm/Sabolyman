class Priority:
    def __init__(self, importance: int = 1):
        self._max_priority = 5
        self._min_priority = 1
        self._value = importance

    @property
    def value(self) -> int:
        return self._value

    def increment_importance(self, increment: int):
        new_importance = self._value + increment
        self._value = max(min(self._max_priority, new_importance), self._min_priority)

    def set(self, importance: int):
        self._value = importance

    @property
    def priority_max(self) -> int:
        return self._max_priority

    @property
    def priority_min(self) -> int:
        return self._min_priority
