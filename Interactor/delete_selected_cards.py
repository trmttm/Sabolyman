from typing import Tuple

from Commands import RemoveCard
from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    command = RemoveCard(e, indexes)
    command.execute()
    if len(indexes) > 0:
        next_selection_index = max(min(indexes) - 1, 0)
        present_card_list(e, p, next_selection_index)
