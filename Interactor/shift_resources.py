from typing import Callable

from Entities.abc_entities import EntitiesABC
from Presenters.abc import PresentersABC
from . import show_action_information


def execute(e: EntitiesABC, p: PresentersABC, shift: int, callback: Callable):
    e.shift_resources(shift)
    show_action_information.execute(e, p, (e.active_action_index,))
    if callback is not None:
        callback(e.selected_resources_indexes)
