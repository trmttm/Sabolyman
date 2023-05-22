from typing import Tuple

from Commands import RemoveAction
from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    command = RemoveAction(e, indexes)
    command.execute()
    if len(indexes) > 0:
        next_selection_indexes = (max(min(indexes) - 1, 0),)
        present_action_list.execute(e, p, next_selection_indexes)
