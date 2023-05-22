from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, color: str, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...]):
    active_card = e.active_card
    if active_card in e.my_cards:
        _set_color_to_cards(e, p, e.get_my_visible_cards_by_indexes(indexes1), color)
    elif active_card in e.their_cards:
        _set_color_to_cards(e, p, e.get_their_visible_cards_by_indexes(indexes2), color)


def _set_color_to_cards(e: EntitiesABC, p: PresentersABC, cards, color):
    for card in cards:
        card.set_color(color)
    present_card_list.execute(e, p)
