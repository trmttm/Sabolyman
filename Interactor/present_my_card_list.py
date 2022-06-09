from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def present_my_card_list(e: EntitiesABC, p: PresentersABC, next_selection_indexes: Tuple[int, ...] = ()):
    my_cards_names = tuple(c.name for c in e.my_cards)
    my_cards_due_dates = tuple(c.due_date for c in e.my_cards)
    completions_status = tuple(c.is_done for c in e.my_cards)

    response_model = my_cards_names, my_cards_due_dates, next_selection_indexes
    p.update_my_cards(*response_model, completions_status=completions_status)
