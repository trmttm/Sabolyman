import datetime
from typing import List
from typing import Optional
from typing import Tuple

from .abc_entity import EntityABC
from .action import Action
from .person import Person


class Actions(EntityABC):
    def __init__(self):
        self._actions: List[Action, ...] = []
        self._active_action = None

    @property
    def action_names(self) -> Tuple[str, ...]:
        return tuple(a.name for a in self._actions)

    @property
    def active_action(self) -> Action:
        return self._active_action

    def set_active_action(self, action: Action):
        self._active_action = action

    def add_new_action(self, action: Action):
        self._actions.append(action)

    def get_action_by_index(self, index: int) -> Action:
        try:
            return self._actions[index]
        except IndexError:
            pass

    @property
    def times_expected(self) -> Tuple[datetime.timedelta, ...]:
        return tuple(a.time_expected for a in self._actions)

    @property
    def times_completed(self) -> Tuple[Optional[datetime.datetime], ...]:
        return tuple(a.time_completed or '' for a in self._actions)

    @property
    def all_actions(self) -> List[Action]:
        return self._actions

    def remove_action(self, action: Action):
        self._actions.remove(action)

    def sort_actions(self, sorted_actions: Tuple[Action, ...]):
        new_actions_list = [c for c in self._actions if c not in sorted_actions]
        new_actions_list += list(sorted_actions)
        self._actions = new_actions_list

    @property
    def current_owner(self) -> Person:
        for action in self._actions:
            if not action.is_done:
                return action.get_owner()
        return Person('No Current Owner')

    @property
    def current_client(self) -> Person:
        for action in self._actions:
            if not action.is_done:
                return action.client
        return Person('No Current Client')

    @property
    def state(self) -> dict:
        actions_state = tuple(a.state for a in self.all_actions)
        active_action_index = 0
        for n, action in enumerate(self.all_actions):
            if action == self.active_action:
                active_action_index = n

        state = {
            'actions_state': actions_state,
            'active_action': active_action_index,
        }
        return state

    def load_state(self, state: dict, alias_actions_dictionary: dict = None):
        self.__init__()
        actions_state = state.get('actions_state', ())
        active_action_index = state.get('active_action', 0)
        for n, action_state in enumerate(actions_state):

            action_id = action_state.get('id')
            if action_id is not None:
                if action_id in alias_actions_dictionary:
                    action = alias_actions_dictionary.get(action_id)
                else:
                    action = Action()
                    alias_actions_dictionary[action_id] = action
            else:
                action = Action()

            action.load_state(action_state)
            self.add_new_action(action)
            if n == active_action_index:
                self._active_action = action
