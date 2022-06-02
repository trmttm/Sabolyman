import datetime

from .file import File
from .files import Files
from .person import Person


class Card:
    def __init__(self):
        self._name = 'New Card'
        self._owner = Person('Name')
        self._importance = 5
        self._due_date = datetime.datetime.today() + datetime.timedelta(1)
        self._is_done = False
        self._files = Files()

    def set_name(self, name: str):
        self._name = name

    def set_owner(self, owner: Person):
        self._owner = owner

    def set_importance(self, importance: int):
        self._importance = importance

    def set_time_expected(self, dead_line: datetime.datetime):
        self._due_date = dead_line

    def mark_done(self):
        self._is_done = True

    def add_file(self, file: File):
        self._files.add_file(file)

    @property
    def name(self) -> str:
        return self._name

    @property
    def due_date(self) -> datetime.datetime:
        return self._due_date
