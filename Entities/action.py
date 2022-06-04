import datetime

from .person import Person


class Action:
    def __init__(self):
        self._name = 'unspecified'
        self._is_done = False
        self._owner = Person('unspecified')
        self._time_expected = datetime.timedelta(1)

    @property
    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def set_owner(self, owner: Person):
        self._owner = owner

    def set_time_expected(self, time_expected: datetime.timedelta):
        self._time_expected = time_expected

    def mark_done(self):
        self._is_done = True

    @property
    def time_expected(self) -> datetime.timedelta:
        return self._time_expected
