import datetime
from typing import List

from .action import Action
from .file import File
from .files import Files
from .person import Person


class Card:
    def __init__(self):
        self._name = 'New Card'
        self._owner = Person('Name')
        self._importance = 5
        self._date_created = datetime.datetime.now()
        self._dead_line = datetime.datetime.today() + datetime.timedelta(1)
        self._is_done = False
        self._actions = []
        self._files = Files()

    def set_name(self, name: str):
        self._name = name

    def set_owner(self, owner: Person):
        self._owner = owner

    def set_importance(self, importance: int):
        self._importance = importance

    def set_dead_line_by_str(self, dead_line_str: str):
        year_str, month_str, day_time_str = dead_line_str.split('/')
        day_str, time_str = day_time_str.split(' ')
        hour_str, minute_str = time_str.split(':')

        year, month, day = int(year_str), int(month_str), int(day_str)
        hour, minute = int(hour_str), int(minute_str)
        dead_line = datetime.datetime(year, month, day, hour, minute)
        self.set_dead_line(dead_line)

    def set_dead_line(self, dead_line: datetime.datetime):
        self._dead_line = dead_line

    def mark_done(self):
        self._is_done = True

    def add_file(self, file: File):
        self._files.add_file(file)

    @property
    def name(self) -> str:
        return self._name

    @property
    def date_created(self) -> datetime.datetime:
        return self._date_created

    @property
    def due_date(self) -> datetime.datetime:
        return self._dead_line

    @property
    def actions(self) -> List[Action]:
        return self._actions
