from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def present_their_card_list(e: EntitiesABC, p: PresentersABC, next_selection_indexes: Tuple[int, ...] = ()):
    their_cards_names = tuple(c.name for c in e.their_cards)
    their_cards_due_dates = tuple(c.due_date for c in e.their_cards)
    completions_status = tuple(c.is_done for c in e.their_cards)

    response_model = their_cards_names, their_cards_due_dates, next_selection_indexes
    p.update_their_cards(*response_model, completions_status=completions_status)
