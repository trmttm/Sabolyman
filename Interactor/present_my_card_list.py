from typing import Tuple

import Utilities

from Entities import EntitiesABC
from Presenters import PresentersABC


def present_my_card_list(e: EntitiesABC, p: PresentersABC, next_selection_indexes: Tuple[int, ...] = ()):
    cards = e.my_visible_cards
    cards_names = tuple(c.name for c in cards)
    sort_by_values = tuple(Utilities.datetime_to_str(c.dead_line) for c in cards)
    status = tuple(c.is_done for c in cards)
    colors = tuple(c.color for c in cards)

    response_model = cards_names, sort_by_values, next_selection_indexes
    p.update_my_cards(*response_model, completions_status=status, colors=colors)
