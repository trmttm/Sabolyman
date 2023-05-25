from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from . import set_action_scheduled


def execute(e: EntitiesABC, p: PresentersABC, scheduled_or_not: bool, actions_indexes: Tuple[int, ...]):
    set_action_scheduled.execute(e, p, scheduled_or_not, actions_indexes)
    # present_action_list.execute(e, p, e.selected_actions_indexes)
    # present_card_list.execute(e, p)
