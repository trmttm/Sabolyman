import datetime
from typing import Callable
from typing import Tuple

from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_action_list
from . import show_action_information
from . import show_card_information


def execute(e: EntitiesABC, p: PresentersABC, getter: Callable, indexes: Tuple[int]):
    if len(indexes) > 0:
        index = indexes[0]
        card: Card = getter(index)
        if card is not None:
            show_card_information.execute(card, e, p)
        else:
            p.update_card_name(e.default_card_name)
            p.update_card_date_created(datetime.datetime.now())
            p.update_card_due_date(e.default_dead_line)
            p.update_card_importance(e.default_importance)

    show_action_information.execute(e, p, (e.active_action_index,))
    present_action_list.execute(e, p, e.selected_actions_indexes)
