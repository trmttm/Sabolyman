import datetime
from typing import List
from typing import Tuple

from .abc_entity import EntityABC
from .action import Action


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
    def all_actions(self) -> List[Action]:
        return self._actions

    def remove_action(self, action: Action):
        self._actions.remove(action)

    def load_state(self, state: dict):
        self.__init__()
        actions_state = state.get('actions_state', ())
        active_action_index = state.get('active_action', 0)
        for n, action_state in enumerate(actions_state):
            action = Action()
            action.load_state(action_state)
            if n == active_action_index:
                self._active_action = action
