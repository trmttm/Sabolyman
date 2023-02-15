from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC
from . import show_my_card_information
from . import show_their_card_information


def execute(card_: Card, e: EntitiesABC, p: PresentersABC):
    if card_ is not None:
        e.set_active_card(card_)
        indexes = (e.active_card_index,)
        if indexes is not None and card_to_jump_to_is_visible(card_, e, indexes):
            if e.active_card_is_in_my_cards:
                show_my_card_information.execute(e, p, indexes)
            else:
                show_their_card_information.execute(e, p, indexes)


def card_to_jump_to_is_visible(card_, e, indexes):
    if e.active_card_is_in_my_cards:
        card_is_visible = (e.get_my_card_by_index(indexes[0]) is card_)
    else:
        card_is_visible = (e.get_their_card_by_index(indexes[0]) is card_)
    return card_is_visible
