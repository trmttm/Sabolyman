from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def present_their_card_list(e: EntitiesABC, p: PresentersABC, next_selection_indexes: Tuple[int, ...] = ()):
    my_cards = e.my_cards

    their_cards_names = tuple(c.name for c in e.all_cards if c not in my_cards)
    their_cards_due_dates = tuple(c.due_date for c in e.all_cards if c not in my_cards)

    response_model = their_cards_names, their_cards_due_dates, next_selection_indexes
    p.update_their_cards(*response_model)
