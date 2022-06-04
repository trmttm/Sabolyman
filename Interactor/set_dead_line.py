from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, dead_line_str: str):
    card = e.active_card
    card.set_dead_line_by_str(dead_line_str)
    present_card_list(e, p)
