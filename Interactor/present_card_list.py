from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_my_card_list import present_my_card_list
from .present_their_card_list import present_their_card_list


def execute(e: EntitiesABC, p: PresentersABC):
    if e.active_card_is_in_my_cards:
        present_their_card_list(e, p, (0,))
        index = get_active_card_location_or_0(e.active_card, e.my_visible_cards)
        present_my_card_list(e, p, (index,))
    elif e.active_card_is_in_their_cards:
        present_my_card_list(e, p, (0,))
        index = get_active_card_location_or_0(e.active_card, e.their_visible_cards)
        present_their_card_list(e, p, (index,))
    e.set_show_this_card(e.active_card)


def get_active_card_location_or_0(active_card, cards_tuple: tuple) -> int:
    try:
        index = cards_tuple.index(active_card)
    except ValueError:
        index = 0
    return index
