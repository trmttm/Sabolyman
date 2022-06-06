from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC

import WidgetNames
from .utilities import datetime_to_str


def execute(v: ViewABC, due_dates: tuple, names: tuple, select_indexes: Tuple[int, ...]):
    v.switch_tree(WidgetNames.tree_my_cards)
    view_model = create_view_model(due_dates, names, select_indexes)
    v.update_tree(view_model)


def create_view_model(due_dates, names, select_indexes: Tuple[int, ...]):
    headings = 'Name', 'Due Date'
    widths = 100, 130
    tree_datas = []
    for n, (name, due_date) in enumerate(zip(names, due_dates)):
        due_date_str = datetime_to_str(due_date)
        tree_datas.append(create_tree_data('', f'{n}', '', (name, due_date_str), (), n in select_indexes))
    stretches = True, False
    scroll_v = True
    scroll_h = True
    view_model = create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)
    return view_model
