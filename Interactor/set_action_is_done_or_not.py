from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_action_list import present_action_list
from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, done_or_not: bool):
    action = e.active_action
    if action is not None:
        if done_or_not:
            action.mark_done()
        else:
            action.mark_not_done()

        p.update_action_is_done(action.is_done)
        present_action_list(e, p)
        present_card_list(e, p)
