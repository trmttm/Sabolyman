from Commands import AddAction
from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC):
    command = AddAction(e)
    command.execute()
    next_selection_indexes = (len(e.active_card.all_actions) - 1,)

    present_action_list.execute(e, p, next_selection_indexes)
