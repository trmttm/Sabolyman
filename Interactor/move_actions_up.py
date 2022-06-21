from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import move_actions


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int, ...]):
    move_actions.execute(e, p, indexes, e.move_actions_up)
