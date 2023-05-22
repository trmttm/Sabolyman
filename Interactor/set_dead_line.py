from typing import Callable
from typing import Tuple

from Entities import Action
from Entities import EntitiesABC
from Presenters import PresentersABC

from . import ask_and_set_datetime_by_str
from . import present_action_list
from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, datetime_str: str, indexes: Tuple[int, ...],
            ask_user: Callable = None):
    update_method = update_actions_dead_lines
    ask_and_set_datetime_by_str.execute(datetime_str, update_method, ask_user, e, p, indexes)


def update_actions_dead_lines(datetime_str: str, actions: Tuple[Action, ...], e: EntitiesABC, p: PresentersABC):
    for action in actions:
        action.set_dead_line_by_str(datetime_str)
        present_card_list.execute(e, p)
        present_action_list.execute(e, p)
