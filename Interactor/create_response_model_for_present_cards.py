from typing import Tuple

from Entities import Card
from Entities import EntitiesABC
from Entities.synchronizer_action_card import SynchronizerABC


def execute(cards: Tuple[Card, ...], e: EntitiesABC, next_selection_indexes) -> Tuple[tuple, dict]:
    sort_by = e.sort_by
    sorter_values = e.sorter_values(cards)
    cards_names = tuple(c.name for c in cards)
    s: SynchronizerABC = e.synchronizer
    args = cards_names, sort_by, sorter_values, next_selection_indexes
    kwargs = {
        'completions_status': tuple(c.is_done for c in cards),
        'colors': tuple(c.color for c in cards),
        'text_colors': tuple('blue' if s.card_has_policy_action(c.id) else 'black' for c in cards),
        'bolds': tuple(True if c.id == e.filter.filter_parent_card_id else False for c in cards),
    }
    return args, kwargs
