from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, hours: int, indexes: Tuple[int, ...]):
    for index_ in indexes:
        action = e.get_action_by_index(index_)
        action.increment_deadline_hours_by(hours)
    present_card_list.execute(e, p)
