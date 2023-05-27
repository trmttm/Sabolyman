from Entities import EntitiesABC
from Entities.synchronizer_action_card import constants
from Presenters import PresentersABC

from . import delete_selected_my_cards
from . import delete_selected_their_cards
from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, **kwargs):
    key_remove_card = constants.REMOVE_CARD
    key_remove_action = constants.REMOVE_ACTION
    key_update_card_list = constants.UPDATE_CARD_LIST
    if kwargs.get(key_remove_card, None):
        card_to_remove = kwargs.get(key_remove_card)
        initial_active_card = e.active_card  # remove side effect 1/2
        e.set_active_card(card_to_remove)
        indexes_ = (e.active_card_index,)
        if e.active_card_is_in_my_cards:
            delete_selected_my_cards.execute(e, p, indexes_)
        else:
            delete_selected_their_cards.execute(e, p, indexes_)
        e.set_active_card(initial_active_card)  # remove side effect 2/2
    elif kwargs.get(key_remove_action, None):
        action_to_remove = kwargs.get(key_remove_action)
        for c in e.all_cards:
            if c.has_action(action_to_remove):
                c.actions.remove_action(action_to_remove)
    elif kwargs.get(key_update_card_list, False):
        present_card_list.execute(e, p)
