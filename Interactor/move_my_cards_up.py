from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from .present_my_card_list import present_my_card_list


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int, ...]):
    destinations = e.move_my_cards_up(indexes)
    present_my_card_list(e, p, destinations)
