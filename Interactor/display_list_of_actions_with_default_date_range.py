import datetime
from typing import Callable

import Utilities
from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC

from . import display_list_of_actions


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, sort_cards: Callable, **kwargs):
    today = datetime.datetime.today()
    january_first = datetime.datetime(today.year, 1, 1)
    from_str = Utilities.datetime_to_str_no_time(january_first)
    to_str = Utilities.datetime_to_str_no_time(today)
    kwargs = {'from': from_str, 'to': to_str, 'owner': e.user.name}
    args = e, g, p, sort_cards
    open_list_of_actions(*args, **kwargs)


def open_list_of_actions(e: EntitiesABC, g: GatewayABC, p: PresentersABC, sort_cards: Callable, **kwargs):
    from_ = Utilities.str_to_date_time_no_time(kwargs.get('from', '2023/1/1'))
    t = Utilities.str_to_date_time_no_time(kwargs.get('to', '2023/6/30'))
    to_ = datetime.datetime(t.year, t.month, t.day, 23, 59)
    owner_name = kwargs.get('owner', 'Taro Yamaka')
    display_list_of_actions.execute(e, g, p, owner_name, from_, to_, sort_cards)
