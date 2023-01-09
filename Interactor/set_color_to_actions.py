from typing import Tuple

from Entities import EntitiesABC
from Interactor import present_action_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, color: str, indexes: Tuple[int, ...]):
    for index_ in indexes:
        action = e.get_action_by_index(index_)
        action.set_color(color)

        present_action_list.execute(e, p, indexes)
