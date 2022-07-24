from typing import Tuple

from Entities import Card
from Entities import EntitiesABC


def execute(cards: Tuple[Card, ...], e: EntitiesABC, next_selection_indexes) -> Tuple[tuple, dict]:
    sort_by = e.sort_by
    sorter_values = e.sorter_values(cards)
    cards_names = tuple(c.name for c in cards)

    args = cards_names, sort_by, sorter_values, next_selection_indexes
    kwargs = {
        'completions_status': tuple(c.is_done for c in cards),
        'colors': tuple(c.color for c in cards),
    }
    return args, kwargs
