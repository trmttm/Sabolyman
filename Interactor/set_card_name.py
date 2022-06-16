from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, card_name: str):
    card = e.active_card
    if card is not None:
        card.set_name(card_name)
        present_card_list.execute(e, p)
