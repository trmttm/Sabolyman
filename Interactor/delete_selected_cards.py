from typing import Callable
from typing import Tuple

from Commands import RemoveCard
from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC


def delete_selected_cards(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int, ...], cards: Tuple[Card, ...],
                          present_method: Callable):
    command = RemoveCard(e, indexes, cards)
    command.execute()
    if len(indexes) > 0:
        next_selection_indexes = (max(min(indexes) - 1, 0),)
        present_method(e, p, next_selection_indexes)
