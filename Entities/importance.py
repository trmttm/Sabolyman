class Importance:
    def __init__(self, importance: int = 1):
        self._max_importance = 5
        self._min_importance = 1
        self._value = importance

    @property
    def value(self) -> int:
        return self._value

    def increment_importance(self, increment: int):
        new_importance = self._value + increment
        self._value = max(min(self._max_importance, new_importance), self._min_importance)

    def set(self, importance: int):
        self._value = importance
