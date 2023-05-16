import datetime
import uuid
from typing import Union

from Utilities import str_to_date_time
from Utilities.tree_data import TreeData

from . import factory1
from .abc_entity import EntityABC
from .file import File
from .files import Files
from .person import Person


class Resources:
    def __init__(self):
        self._resources = TreeData()

    @property
    def data(self) -> TreeData:
        return self._resources

    def add_action_resources(self, names: tuple, uris: tuple):
        for name, uri in zip(names, uris):
            if uri not in self._resources.data:
                self._resources.add_data(name, uri)


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
        self._color_set_by_user = self._color
        self._client = Person('')
        self._dead_line = datetime.datetime(tm.year, tm.month, tm.day, 17)
        self._start_from = self._date_created
        self._resources = Resources()
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

    def get_owner(self) -> Person:
        return self._owner

    @property
    def is_done(self) -> bool:
        return self._is_done

    @property
    def date_created(self) -> datetime.datetime:
        return self._date_created

    def mark_done(self):
        self.mark_done_programmatically()

    def mark_not_done(self):
        self.mark_not_done_programmatically()

    def mark_done_programmatically(self):
        # Not subject to synchronizer wrapper
        self._is_done = True

    def mark_not_done_programmatically(self):
        # Not subject to synchronizer wrapper
        self._is_done = False
        self._time_completed = None

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
            self._set_color_without_side_effects('Yellow')
        return score

    def get_search_undone_owner_result(self, search_key: str) -> int:
        score = 0
        if not self._is_done and (search_key.lower() in self._owner.name.lower()):
            score += 10
        if score > 0:
            self._set_color_without_side_effects('Yellow')
        return score

    def get_search_owner_result(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._owner.name.lower():
            score += 10
        if score > 0:
            self._set_color_without_side_effects('Yellow')
        return score

    def get_search_action_name(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self.name.lower():
            score += 10
        if score > 0:
            self._set_color_without_side_effects('Yellow')
        return score

    def get_search_action_client_name(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._client.name.lower():
            score += 10
        if score > 0:
            self._set_color_without_side_effects('Yellow')
        return score

    def set_color(self, color: str):
        self._set_color_without_side_effects(color)

    def _set_color_without_side_effects(self, color):
        # set_color will be wrapped by synchronizer, causing infinite recursion of present cards
        self._color = color

    def register_as_user_set_color(self):
        self._color_set_by_user = self._color

    def set_true_color(self):
        self._set_color_without_side_effects(self._color_set_by_user)

    def clear_search_highlight(self):
        self._set_color_without_side_effects(self._color_set_by_user)

    @property
    def color(self) -> str:
        return self._color or 'white'

    def set_client(self, client: Person):
        self._client = client

    @property
    def client(self) -> Person:
        return self._client

    def set_dead_line_by_str(self, dead_line_str: str):
        self.set_dead_line(str_to_date_time(dead_line_str))

    def set_dead_line(self, dead_line: datetime.datetime):
        self.set_dead_line_programmatically(dead_line)

    def set_dead_line_programmatically(self, dead_line: datetime.datetime):
        self._dead_line = dead_line

    def increment_deadline_by(self, days: int):
        new_dead_line = self._dead_line + datetime.timedelta(days)
        self.set_dead_line(new_dead_line)

    def increment_deadline_hours_by(self, hours: int):
        self._dead_line += datetime.timedelta(0, hours * 60 * 60)

    def get_dead_line(self) -> datetime.datetime:
        return self.get_dead_line_programmatically()

    def get_dead_line_programmatically(self):
        return self._dead_line

    def set_start_from_by_str(self, start_from_str: str):
        self.set_start_from(str_to_date_time(start_from_str))

    def update_date_start(self):
        self._start_from = datetime.datetime.now()

    def set_start_from(self, start_from: datetime.datetime):
        self._start_from = start_from

    def increment_start_from_by(self, days: int):
        new_start_from = self._start_from + datetime.timedelta(days)
        self.set_start_from(new_start_from)

    def increment_start_from_hours_by(self, hours: int):
        self._start_from += datetime.timedelta(0, hours * 60 * 60)

    def get_start_from(self) -> datetime.datetime:
        return self._start_from

    def update_date_created(self):
        self._date_created = datetime.datetime.now()

    def set_id(self):
        if self._id is None:
            self._id = str(uuid.uuid4())

    def force_set_id(self):
        self._id = str(uuid.uuid4())

    @property
    def id(self) -> str:
        if self._id is None:
            self.set_id()
        return self._id

    def select_action_resources(self, indexes: tuple):
        self._resources.data.select_data_by_indexes(indexes)

    @property
    def selected_resources_indexes(self) -> tuple:
        return self._resources.data.selected_indexes

    def add_action_resources(self, names: tuple, uris: tuple):
        self._resources.add_action_resources(names, uris)

    def remove_selected_action_resources(self):
        self._resources.data.remove_selected()

    def shift_resources(self, shift: int):
        self._resources.data.sort_data(shift)

    def get_action_resource_names(self) -> tuple[tuple, tuple]:
        return self._resources.data.names

    def get_action_resource_datas(self) -> tuple[tuple, tuple]:
        return self._resources.data.data

    def get_selected_resources(self) -> tuple[tuple, tuple]:
        return self._resources.data.selected_datas

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
            'start_from': self._start_from,
            'id': self._id,
            'color': self._color,
            'resources': self._resources.data.state,
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
        self._start_from = state.get('start_from', self._date_created)
        self._id = state.get('id', None)
        self._color = state.get('color', 'White')
        self._color_set_by_user = self._color
        self._resources.data.set_state(state.get('resources', Resources().data.state))

    def __repr__(self):
        return self._name
