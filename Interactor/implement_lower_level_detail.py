from Commands import AddCard
from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_my_card_list import present_my_card_list


def execute(e: EntitiesABC, p: PresentersABC):
    action_policy = e.active_action
    command = AddCard(e)
    command.execute()
    card_implementation = e.active_card

    # Implement a solution to synchronize action_policy and new_card
    '''
    What happens when
    1) action_policy state is changed?
        deadline is extended
        deadline is shortened -> balls at their court must be modified.
    2) card_implementation state is changed?
    3) action_policy is deleted
        all of the lower_level actions at their court must be notified to cancel.
    4) card_implementation is deleted
        high level policy action can also be deleted?
        
    ...fix the semantics first.
    '''

    next_selection_indexes = (len(e.my_visible_cards) - 1,)
    present_my_card_list(e, p, next_selection_indexes)
