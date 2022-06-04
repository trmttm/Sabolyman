from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    if len(indexes) > 0:
        index = indexes[0]
        card = e.get_card_by_index(index)
        if card is not None:
            e.set_active_card(card)

            p.update_card_name(card.name)
            p.update_card_date_created(card.date_created)
            p.update_card_due_date(card.due_date)
            p.updates_card_actions()
