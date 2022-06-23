import Utilities

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, time_expected_str: str):
    action = e.active_action
    if action is not None:
        time_expected = Utilities.time_delta_str_to_time_delta(time_expected_str)
        action.set_time_expected(time_expected)
        present_action_list.execute(e, p, (e.active_action_index,))
