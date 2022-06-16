from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, action_name: str):
    action = e.active_action
    if action is not None:
        action.set_name(action_name)
        present_action_list.execute(e, p)
