from Entities import EntitiesABC
from Entities.synchronizer_action_card import constants
from Presenters import PresentersABC
from . import delete_selected_my_cards
from . import delete_selected_their_cards

from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, **kwargs):
    if kwargs.get(constants.REMOVE_CARD, None):
        card_to_remove = kwargs.get(constants.REMOVE_CARD)
        initial_active_card = e.active_card
        e.set_active_card(card_to_remove)
        indexes_ = (e.active_card_index,)
        if e.active_card_is_in_my_cards:
            delete_selected_my_cards.execute(e, p, indexes_)
        else:
            delete_selected_their_cards.execute(e, p, indexes_)
        e.set_active_card(initial_active_card)
    elif kwargs.get(constants.UPDATE_CARD_LIST, False):
        present_card_list.execute(e, p)
