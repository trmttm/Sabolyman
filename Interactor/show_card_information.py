from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(card: Card, e: EntitiesABC, p: PresentersABC):
    e.set_active_card(card)
    p.update_card_name(card.name)
    p.update_card_date_created(card.date_created)
    p.update_card_due_date(card.dead_line)
    p.update_card_importance(card.get_priority())
