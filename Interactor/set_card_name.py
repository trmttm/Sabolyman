from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, card_name: str):
    card = e.active_card
    card.set_name(card_name)
    present_card_list(e, p)
