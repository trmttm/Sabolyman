import datetime
from typing import Tuple

from Entities import EntitiesABC


def execute(e: EntitiesABC, done_or_not, actions_indexes: Tuple[int, ...] = None):
    if actions_indexes is None:
        actions_indexes = (e.active_action_index,)
    for i, action in enumerate(e.active_card.all_actions):
        if i in actions_indexes:
            if done_or_not and action.is_done and action.time_completed is None:
                # note that action mark done may be prevented if its policy action
                action.set_completed_time(datetime.datetime.now())
            if not done_or_not and not action.is_done:  # just cuz done_or_not is False does not always set_incomplete
                action.set_incomplete()
