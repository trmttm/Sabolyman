from typing import Tuple

from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC
from .delete_selected_cards import delete_selected_cards
from .present_their_card_list import present_their_card_list


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int, ...], cards: Tuple[Card, ...]):
    present_method = present_their_card_list
    delete_selected_cards(e, p, indexes, cards, present_method)
