from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int, ...]):
    destinations = e.move_actions_down(indexes)
    present_action_list.execute(e, p, destinations)
