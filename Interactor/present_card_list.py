from Entities import EntitiesABC
from Interactor.present_my_card_list import present_my_card_list
from Interactor.present_their_card_list import present_their_card_list
from Presenters import PresentersABC


def present_card_list(e: EntitiesABC, p: PresentersABC):
    if e.active_card_is_in_my_cards:
        present_their_card_list(e, p, (0,))
        present_my_card_list(e, p, (e.my_cards.index(e.active_card),))
    elif e.active_card_is_in_their_cards:
        present_my_card_list(e, p, (0,))
        present_their_card_list(e, p, (e.their_cards.index(e.active_card),))
