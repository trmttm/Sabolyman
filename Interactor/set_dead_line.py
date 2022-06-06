from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_my_card_list import present_my_card_list
from .present_their_card_list import present_their_card_list


def execute(e: EntitiesABC, p: PresentersABC, dead_line_str: str):
    card = e.active_card
    if card is not None:
        card.set_dead_line_by_str(dead_line_str)
        present_my_card_list(e, p)
        present_their_card_list(e, p)
