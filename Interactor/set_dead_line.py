from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, dead_line_str: str, trees_selected_indexes: Tuple[Tuple[int, ...], ...]):
    card = e.active_card
    if card is not None:
        if e.active_card_is_in_my_cards:
            indexes = trees_selected_indexes[0]
            cards = tuple(e.get_my_card_by_index(i) for i in indexes)
        else:
            indexes = trees_selected_indexes[1]
            cards = tuple(e.get_their_card_by_index(i) for i in indexes)
        for card in cards:
            card.set_dead_line_by_str(dead_line_str)
            present_card_list.execute(e, p)
