from typing import Callable
from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_action_list
from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int, ...], move_method: Callable):
    destinations = move_method(indexes)
    e.active_card.select_actions(destinations)
    present_card_list.execute(e, p)
    present_action_list.execute(e, p, destinations)
