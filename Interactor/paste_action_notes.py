from Entities import EntitiesABC
from Presenters import PresentersABC

from . import show_action_information


def execute(e: EntitiesABC, p: PresentersABC):
    copied_actions = e.copied_actions
    if len(copied_actions) > 0:
        copied_action = copied_actions[0]
        e.active_action.add_description(copied_action.description)
        show_action_information.execute(e, p, (e.active_action_index,))
