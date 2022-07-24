from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import create_response_model_for_present_cards


def present_my_card_list(e: EntitiesABC, p: PresentersABC, next_selection_indexes: Tuple[int, ...] = ()):
    cards = e.my_visible_cards
    args, kwargs = create_response_model_for_present_cards.execute(cards, e, next_selection_indexes)
    p.update_my_cards(*args, **kwargs)
