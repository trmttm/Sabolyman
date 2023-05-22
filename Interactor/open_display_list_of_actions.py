import datetime
from typing import Callable

import Utilities
from Entities.abc_entities import EntitiesABC
from . import display_list_of_actions
from Presenters.abc import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, sort_cards: Callable):
    def callback(**state):
        from_ = Utilities.str_to_date_time_no_time(state['from'])
        to_ = Utilities.str_to_date_time_no_time(state['to'])
        owner_name = state['owner']
        display_list_of_actions.execute(e, p, owner_name, from_, to_, sort_cards)

    default_from = '2023/01/01'
    default_to = Utilities.datetime_to_str_no_time(datetime.datetime.today())
    default_owner = e.user.name
    default_values = {'from': default_from, 'to': default_to, 'owner': default_owner}
    p.ask_user_from_to_owner(callback, **default_values)
