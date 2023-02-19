from Commands import AddCard
from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_my_card_list import present_my_card_list


def execute(e: EntitiesABC, p: PresentersABC):
    action_policy = e.active_action

    command = AddCard(e)
    command.execute()
    card_implementation = e.active_card

    e.synchronize_card_to_action(action_policy, card_implementation)

    next_selection_indexes = (len(e.my_visible_cards) - 1,)
    present_my_card_list(e, p, next_selection_indexes)
