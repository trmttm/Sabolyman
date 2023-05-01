from Entities import EntitiesABC
from Presenters import PresentersABC

from . import show_action_information


def execute(e: EntitiesABC, p: PresentersABC):
    copied_actions = e.copied_actions
    if len(copied_actions) > 0:
        copied_action = copied_actions[0]
        names = copied_action.get_action_resource_names()
        uris = copied_action.get_action_resource_datas()
        e.active_action.add_action_resources(names, uris)
        show_action_information.execute(e, p, (e.active_action_index,))
