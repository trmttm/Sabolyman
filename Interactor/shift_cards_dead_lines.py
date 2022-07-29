from typing import Tuple

from Entities import EntitiesABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, days: int, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...]):
    active_card = e.active_card
    if active_card in e.my_cards:
        cards_ = e.get_my_visible_cards_by_indexes(indexes1)
        _shift_cards_dead_lines(cards_, days)
    elif active_card in e.their_cards:
        cards_ = e.get_their_visible_cards_by_indexes(indexes2)
        _shift_cards_dead_lines(cards_, days)
    present_card_list.execute(e, p)


def _shift_cards_dead_lines(cards, days: int):
    for card in cards:
        for action in card.all_actions:
            if not action.is_done:
                action.increment_deadline_by(days)
