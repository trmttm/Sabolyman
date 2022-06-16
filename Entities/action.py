import datetime
from typing import Union

from . import factory1
from .abc_entity import EntityABC
from .file import File
from .files import Files
from .person import Person


class Action(EntityABC):

    def __init__(self):
        self._name = 'unspecified'
        self._is_done = False
        self._owner = Person('unspecified')
        self._time_expected = datetime.timedelta(1)
        self._date_created = datetime.datetime.now()
        self._description = ''
        self._files = Files()
        self._completed_time = None

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
        self._completed_time = when

    def set_incomplete(self):
        self._completed_time = None

    @property
    def time_completed(self) -> Union[None, datetime.datetime]:
        return self._completed_time

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
            'completed_time': self._completed_time,
        }
        return state

    def load_state(self, state: dict):
        self._name = state.get('name', '')
        self._is_done = state.get('is_done', False)
        self._owner = factory1.factory_person(state, 'owner')
        self._time_expected = state.get('time_expected', datetime.timedelta(1))
        self._date_created = state.get('date_created', datetime.datetime.today())
        self._description = state.get('description', '')
        self._files = factory1.factory_files(state)
        self._completed_time = state.get('completed_time', None)
