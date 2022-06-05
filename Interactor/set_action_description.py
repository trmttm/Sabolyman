from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, description: str):
    action = e.active_action
    if action is not None:
        action.add_description(description)
