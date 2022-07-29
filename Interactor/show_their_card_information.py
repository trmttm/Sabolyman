from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import get_card_index
from .show_card_information import display_card_information


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    indexes = get_card_index.execute(e, e.their_visible_cards, indexes)
    if indexes is not None:
        p.deselect_my_cards()
        getter = e.get_their_card_by_index
        display_card_information(e, p, getter, indexes)
