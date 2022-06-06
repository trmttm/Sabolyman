from typing import Tuple

from Commands import RemoveCard
from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_my_card_list import present_my_card_list
from .present_their_card_list import present_their_card_list


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    command = RemoveCard(e, indexes)
    command.execute()
    if len(indexes) > 0:
        next_selection_indexes = (max(min(indexes) - 1, 0),)
        present_my_card_list(e, p, next_selection_indexes)
        present_their_card_list(e, p, next_selection_indexes)
