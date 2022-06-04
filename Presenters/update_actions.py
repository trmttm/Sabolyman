from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC

import WidgetNames
from .utilities import time_delta_to_str


def execute(v: ViewABC, due_dates: tuple, names: tuple, select_nth: int):
    v.switch_tree(WidgetNames.tree_card_actions)
    view_model = create_view_model(due_dates, names, select_nth)
    v.update_tree(view_model)


def create_view_model(due_dates, names, select_nth):
    headings = 'Name', 'Time expected'
    widths = 100, 130
    tree_dates = []
    for n, (name, due_date) in enumerate(zip(names, due_dates)):
        d = due_date
        due_date_str = time_delta_to_str(d)
        tree_dates.append(create_tree_data('', f'{n}', '', (name, due_date_str), (), n == select_nth))
    stretches = True, False
    scroll_v = True
    scroll_h = True
    view_model = create_view_model_tree(headings, widths, tree_dates, stretches, scroll_v, scroll_h)
    return view_model
