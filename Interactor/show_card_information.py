import datetime
from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    if len(indexes) > 0:
        index = indexes[0]
        card = e.get_card_by_index(index)
        if card is not None:
            e.set_active_card(card)
            action_names = e.action_names
            times_expected = e.times_expected

            p.update_card_name(card.name)
            p.update_card_date_created(card.date_created)
            p.update_card_due_date(card.due_date)
            p.updates_card_actions(action_names, times_expected)
        else:
            p.update_card_name(e.default_card_name)
            p.update_card_date_created(datetime.datetime.now())
            p.update_card_due_date(e.default_dead_line)
            p.updates_card_actions((), ())
