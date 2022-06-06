from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from .show_card_information import display_card_information


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    getter = e.get_their_card_by_index
    display_card_information(e, p, getter, indexes)
