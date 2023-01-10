from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, color: str, indexes: Tuple[int, ...]):
    for index_ in indexes:
        action = e.get_action_by_index(index_)
        action.set_color(color)
        action.register_as_user_set_color()

        present_action_list.execute(e, p, indexes)
