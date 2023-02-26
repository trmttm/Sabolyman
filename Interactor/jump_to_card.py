from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC
from . import show_my_card_information
from . import show_their_card_information


def execute(card_: Card, e: EntitiesABC, p: PresentersABC):
    if (card_ is not None) and e.card_is_visible(card_):
        e.set_active_card(card_)
        indexes = (e.active_card_index,)
        if e.active_card_is_in_my_cards:
            show_my_card_information.execute(e, p, indexes)
        else:
            show_their_card_information.execute(e, p, indexes)
