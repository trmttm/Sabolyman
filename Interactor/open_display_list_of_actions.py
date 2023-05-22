import datetime
from typing import Callable

import Utilities
from Entities.abc_entities import EntitiesABC
from Presenters.abc import PresentersABC

from . import display_list_of_actions


def execute(e: EntitiesABC, p: PresentersABC, sort_cards: Callable):
    def callback(**state):
        from_ = Utilities.str_to_date_time_no_time(state['from'])
        t = Utilities.str_to_date_time_no_time(state['to'])
        to_ = datetime.datetime(t.year, t.month, t.day, 23, 59)
        owner_name = state['owner']
        display_list_of_actions.execute(e, p, owner_name, from_, to_, sort_cards)

    default_from = '2023/01/01'
    default_to = Utilities.datetime_to_str_no_time(datetime.datetime.today())
    default_owner = e.user.name
    default_values = {'from': default_from, 'to': default_to, 'owner': default_owner}
    p.ask_user_from_to_owner(callback, **default_values)
