from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, action_name: str, actions_indexes: Tuple[int, ...]):
    if actions_indexes is None:
        actions_indexes = (e.active_action_index,)
    for i, action in enumerate(e.active_card.all_actions):
        if i in actions_indexes:
            action.set_name(action_name)
            present_action_list.execute(e, p, e.selected_actions_indexes)
