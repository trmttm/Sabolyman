from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, scheduled_or_not: bool, actions_indexes: Tuple[int, ...]):
    if actions_indexes is None:
        actions_indexes = (e.active_action_index,)
    for i, action in enumerate(e.active_card.all_actions):
        if i in actions_indexes:
            if scheduled_or_not:
                action.mark_scheduled()
            else:
                action.mark_not_scheduled()

            p.update_action_is_done(action.is_done)
