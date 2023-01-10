from Commands import DuplicateAction
from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC):
    copied_actions = e.copied_actions
    for action in copied_actions:
        command = DuplicateAction(e, action)
        command.execute()

    n_new_actions = len(copied_actions)
    n_all_actions = len(e.active_card.all_actions)
    next_selection_index = tuple(n_all_actions - n_new_actions + i for i in range(n_new_actions))
    present_action_list.execute(e, p, next_selection_index)
