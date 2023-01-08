import datetime
import uuid
from typing import Union

from . import factory1
from .abc_entity import EntityABC
from .file import File
from .files import Files
from .person import Person


class Action(EntityABC):

    def __init__(self):
        tm = datetime.datetime.today() + datetime.timedelta(1)
        self._name = 'unspecified'
        self._is_done = False
        self._owner = Person('unspecified')
        self._time_expected = datetime.timedelta(1)
        self._date_created = datetime.datetime.now()
        self._description = ''
        self._files = Files()
        self._time_completed = None
        self._color = 'White'
        self._client = Person('')
        self._dead_line = datetime.datetime(tm.year, tm.month, tm.day, 17)
        self._id = None

    @property
    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def set_owner(self, owner: Person):
        self._owner = owner

    def set_time_expected(self, time_expected: datetime.timedelta):
        self._time_expected = time_expected

    def set_completed_time(self, when: datetime.datetime):
        self._time_completed = when

    def set_incomplete(self):
        self._time_completed = None

    @property
    def time_completed(self) -> Union[None, datetime.datetime]:
        if self._time_completed is None and self.is_done:
            self.set_completed_time(datetime.datetime.now())
        return self._time_completed

    @property
    def owner(self) -> Person:
        return self._owner

    @property
    def is_done(self) -> bool:
        return self._is_done

    @property
    def date_created(self) -> datetime.datetime:
        return self._date_created

    def mark_done(self):
        self._is_done = True

    def mark_not_done(self):
        self._is_done = False

    @property
    def time_expected(self) -> datetime.timedelta:
        return self._time_expected

    @property
    def description(self) -> str:
        return self._description

    def add_description(self, description: str):
        self._description = description

    def add_file(self, file: File):
        self._files.add_file(file)

    @property
    def files(self) -> Files:
        return self._files

    def get_search_all_result(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._name.lower():
            score += 10
        if search_key.lower() in self._description.lower():
            score += 5
        if search_key.lower() in self._owner.name.lower():
            score += 5
        if score > 0:
            self.set_color('Yellow')
        return score

    def get_search_undone_owner_result(self, search_key: str) -> int:
        score = 0
        if not self._is_done and (search_key.lower() in self._owner.name.lower()):
            score += 10
        if score > 0:
            self.set_color('Yellow')
        return score

    def get_search_owner_result(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._owner.name.lower():
            score += 10
        if score > 0:
            self.set_color('Yellow')
        return score

    def get_search_action_name(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self.name.lower():
            score += 10
        if score > 0:
            self.set_color('Yellow')
        return score

    def get_search_action_client_name(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._client.name.lower():
            score += 10
        if score > 0:
            self.set_color('Yellow')
        return score

    def set_color(self, color: str):
        self._color = color

    def remove_color(self):
        self._color = 'White'

    @property
    def color(self) -> str:
        return self._color

    def set_client(self, client: Person):
        self._client = client

    @property
    def client(self) -> Person:
        return self._client

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

    def increment_deadline_by(self, days: int):
        self._dead_line += datetime.timedelta(days)

    def increment_deadline_hours_by(self, hours: int):
        self._dead_line += datetime.timedelta(0, hours * 60 * 60)

    @property
    def dead_line(self) -> datetime.datetime:
        return self._dead_line

    def update_date_created(self):
        self._date_created = datetime.datetime.now()

    def set_id(self):
        self._id = str(uuid.uuid4())

    @property
    def state(self) -> dict:
        state = {
            'name': self._name,
            'is_done': self._is_done,
            'owner': self._owner.state,
            'time_expected': self._time_expected,
            'date_created': self._date_created,
            'description': self._description,
            'files': self._files.state,
            'client': self._client.state,
            'completed_time': self.time_completed,
            'dead_line': self._dead_line,
            'id': self._id,
        }
        return state

    def load_state(self, state: dict):
        tm = datetime.datetime.today() + datetime.timedelta(1)
        self._name = state.get('name', '')
        self._is_done = state.get('is_done', False)
        self._owner = factory1.factory_person(state, 'owner')
        self._time_expected = state.get('time_expected', datetime.timedelta(1))
        self._date_created = state.get('date_created', datetime.datetime.today())
        self._description = state.get('description', '')
        self._files = factory1.factory_files(state)
        self._client = factory1.factory_person(state, 'client')
        self._time_completed = state.get('completed_time', None)
        self._dead_line = state.get('dead_line', datetime.datetime(tm.year, tm.month, tm.day, 17, 0))
        self._id = state.get('id', None)

    def __repr__(self):
        return self._name
