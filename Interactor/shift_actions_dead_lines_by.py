from typing import Tuple

from Entities import EntitiesABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, days: int, indexes: Tuple[int, ...]):
    for index_ in indexes:
        action = e.get_action_by_index(index_)
        action.increment_deadline_by(days)
    present_card_list.execute(e, p)
