import datetime
import uuid
from typing import List
from typing import Tuple

from . import factory1
from . import factory2
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
        self._actions = Actions()
        self._files = Files()
        self._color = None
        self._selected_actions_indexes = ()
        self._id = None

    def set_name(self, name: str):
        self._name = name

    def set_owner(self, owner: Person):
        self._owner = owner

    @property
    def owner(self) -> Person:
        for action in self.actions.all_actions:
            if not action.is_done:
                return action.owner
        return self._owner

    def set_importance(self, importance: int):
        self._importance = importance

    def set_color(self, color):
        self._color = color

    @property
    def color(self):
        return self._color or 'white'

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

    def update_date_created(self):
        self._date_created = datetime.datetime.now()

    def reset_starting_date_to_today(self):
        self.reset_starting_date_to(datetime.datetime.today().date())

    def reset_starting_date_to(self, date: datetime.date):
        all_dead_lines = tuple(a.get_dead_line() for a in self.all_actions)
        if len(all_dead_lines) > 0:
            delta_days = max(tuple(date - dead_line.date() for dead_line in all_dead_lines))
            new_dead_lines = tuple(dead_line + delta_days for dead_line in all_dead_lines)
            for new_deadline, action in zip(new_dead_lines, self.all_actions):
                action.set_dead_line(new_deadline)

    @property
    def dead_line(self) -> datetime.datetime:
        return self.dead_line_min()

    def dead_line_min(self):
        return self._dead_line(min)

    def dead_line_max(self):
        return self._dead_line(max)

    def _dead_line(self, max_or_min):
        all_actions = self._actions.all_actions
        undone_actions = tuple(a for a in all_actions if not a.is_done)
        try:
            dead_line = max_or_min(a.get_dead_line() for a in undone_actions)
        except ValueError:
            dead_line = datetime.datetime.today() + datetime.timedelta(1)
        return dead_line

    def increment_deadline_by(self, days: int):
        for action in self.all_actions:
            if not action.is_done:
                action.increment_deadline_by(days)

    @property
    def all_actions(self) -> List[Action]:
        return self._actions.all_actions

    @property
    def actions(self) -> Actions:
        return self._actions

    def add_action(self, action: Action):
        self._actions.add_new_action(action)

    @property
    def is_done(self) -> bool:
        all_actions = self._actions.all_actions
        if len(all_actions) == 0:
            return False
        for action in all_actions:
            if not action.is_done:
                return False
        return True

    def select_actions(self, indexes: Tuple[int, ...]):
        self._selected_actions_indexes = indexes

    @property
    def selected_actions(self) -> Tuple[Action, ...]:
        return tuple(self._actions.get_action_by_index(i) for i in self._selected_actions_indexes)

    @property
    def selected_actions_indexes(self) -> Tuple[int, ...]:
        return self._selected_actions_indexes

    def get_search_all_result(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._name.lower():
            score += 100
        for action in self.actions.all_actions:  # Set score by action properties
            score += action.get_search_all_result(search_key)
        return score

    def get_search_undone_owner_result(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._owner.name.lower():
            score += 100
        for action in self.actions.all_actions:  # Set score by action properties
            score += action.get_search_undone_owner_result(search_key)
        return score

    def get_search_owner_result(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self._owner.name.lower():
            score += 100
        for action in self.actions.all_actions:  # Set score by action properties
            score += action.get_search_owner_result(search_key)
        return score

    def get_search_action_name(self, search_key: str) -> int:
        score = 0
        for action in self.actions.all_actions:
            score += action.get_search_action_name(search_key)
        return score

    def get_search_card_name(self, search_key: str) -> int:
        score = 0
        if search_key.lower() in self.name.lower():
            score += 100
        return score

    def get_search_action_client_name(self, search_key: str) -> int:
        score = 0
        for action in self.actions.all_actions:
            score += action.get_search_action_client_name(search_key)
        return score

    def set_actions_true_colors(self):
        for action in self._actions.all_actions:
            action.set_true_color()

    def clear_actions_highlight(self):
        for action in self._actions.all_actions:
            action.clear_search_highlight()

    @property
    def current_owner(self) -> Person:
        return self._actions.current_owner

    @property
    def current_client(self) -> Person:
        return self._actions.current_client

    def set_id(self):
        if self._id is None:
            self._id = str(uuid.uuid4())

    @property
    def id(self) -> str:
        if self._id is None:
            self.set_id()
        return self._id

    def has_action(self, action_: Action) -> bool:
        return action_ in self._actions.all_actions

    @property
    def state(self) -> dict:
        state = {
            'name': self._name,
            'importance': self._importance,
            'date_created': self._date_created,
            'owner': self._owner.state,
            'actions': self._actions.state,
            'files': self._files.state,
            'color': self._color,
            'selected_action_indexes': self._selected_actions_indexes,
            'id': self._id,
        }
        return state

    def load_state(self, state: dict, alias_actions_dictionary: dict = None):
        self._name = state.get('name', '')
        self._owner = factory1.factory_person(state, 'owner')
        self._importance = state.get('importance', '')
        self._date_created = state.get('date_created', datetime.datetime.today())
        self._actions = factory2.factory_actions(state, alias_actions_dictionary)
        self._files = factory1.factory_files(state)
        self._color = state.get('color', None)
        self._selected_actions_indexes = state.get('selected_action_indexes', ())
        self._id = state.get('id', None)

    def __repr__(self):
        return self._name

    def __lt__(self, other) -> bool:
        return self.name < other.name
