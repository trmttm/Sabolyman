from typing import Tuple

from Entities import EntitiesABC


def execute(e: EntitiesABC, indexes: Tuple[int, ...]):
    e.active_card.select_actions(indexes)
