import datetime
from typing import Tuple

from Entities import EntitiesABC


def execute(e: EntitiesABC, done_or_not, actions_indexes: Tuple[int, ...] = None):
    if actions_indexes is None:
        actions_indexes = (e.active_action_index,)
    for i, action in enumerate(e.active_card.all_actions):
        if i in actions_indexes:
            if done_or_not:
                action.set_completed_time(datetime.datetime.now())
            else:
                action.set_incomplete()
