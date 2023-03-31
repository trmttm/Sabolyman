from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, increment: int):
    active_card = e.active_card
    active_card.increment_priority(increment)
    p.update_card_importance(active_card.get_priority())
