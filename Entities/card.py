import datetime

import Entities.factory2
from . import factory1
from .abc_entity import EntityABC
from .action import Action
from .actions import Actions
from .file import File
from .files import Files
from .person import Person


class Card(EntityABC):

    def __init__(self):
        self._name = 'New Card'
        self._owner = Person('Name')
        self._importance = 5
        self._date_created = datetime.datetime.now()
        self._dead_line = datetime.datetime.today() + datetime.timedelta(1)
        self._is_done = False
        self._actions = Actions()
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
    def files(self) -> Files:
        return self._files

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
    def actions(self) -> Actions:
        return self._actions

    def add_action(self, action: Action):
        self._actions.add_new_action(action)

    @property
    def state(self) -> dict:
        state = {
            'name': self._name,
            'importance': self._importance,
            'date_created': self._date_created,
            'dead_line': self._dead_line,
            'is_done': self._is_done,
            'owner': self._owner.state,
            'actions': self._actions.state,
            'files': self._files.state,
        }
        return state

    def load_state(self, state: dict):
        self._name = state.get('name', '')
        self._owner = factory1.factory_person(state, 'onwer')
        self._importance = state.get('importance', '')
        self._date_created = state.get('date_created', datetime.datetime.today())
        self._dead_line = state.get('dead_line', '')
        self._is_done = state.get('is_done', False)
        self._actions = Entities.factory2.factory_actions(state)
        self._files = factory1.factory_files(state)
