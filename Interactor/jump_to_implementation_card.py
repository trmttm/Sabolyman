from Entities import EntitiesABC
from Presenters import PresentersABC
from . import jump_to_card


def execute(e: EntitiesABC, p: PresentersABC, callback):
    action = e.active_action
    if action is not None:
        implementation_card = e.get_implementation_card(action.id)
        jump_to_card.execute(implementation_card, e, p)
    callback()
