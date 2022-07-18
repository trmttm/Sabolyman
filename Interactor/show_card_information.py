import datetime
from typing import Callable
from typing import Tuple

from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list
from . import show_action_information


def display_card_information(e: EntitiesABC, p: PresentersABC, getter: Callable, indexes: Tuple[int]):
    if len(indexes) > 0:
        index = indexes[0]
        card: Card = getter(index)
        if card is not None:
            e.set_active_card(card)

            p.update_card_name(card.name)
            p.update_card_date_created(card.date_created)
            p.update_card_due_date(card.due_date)
        else:
            p.update_card_name(e.default_card_name)
            p.update_card_date_created(datetime.datetime.now())
            p.update_card_due_date(e.default_dead_line)

    show_action_information.execute(e, p, (e.active_action_index,))
    present_action_list.execute(e, p, e.selected_actions_indexes)
