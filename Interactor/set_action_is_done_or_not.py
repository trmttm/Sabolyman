from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, done_or_not: bool, actions_indexes: Tuple[int, ...]):
    if actions_indexes is None:
        actions_indexes = (e.active_action_index,)
    for i, action in enumerate(e.active_card.all_actions):
        if i in actions_indexes:
            if done_or_not:
                action.mark_done()
            else:
                action.mark_not_done()

            p.update_action_is_done(action.is_done)
