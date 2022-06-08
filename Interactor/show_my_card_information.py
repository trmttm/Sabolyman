from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from .show_card_information import display_card_information


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    p.deselect_their_cards()
    getter = e.get_my_card_by_index
    display_card_information(e, p, getter, indexes)
