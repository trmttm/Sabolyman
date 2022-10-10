from typing import Tuple

from Entities import EntitiesABC


def execute(e: EntitiesABC, left_indexes_and_right_indexes: Tuple[Tuple[int, ...], ...]):
    left_indexes, right_indexes = left_indexes_and_right_indexes
    if e.active_card_is_in_my_cards:
        indexes = left_indexes
        all_cards = e.my_visible_cards
    else:
        indexes = right_indexes
        all_cards = e.their_visible_cards
    return all_cards, indexes
