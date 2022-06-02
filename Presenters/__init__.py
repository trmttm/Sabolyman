import datetime
from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC


class Presenters:
    def __init__(self, view: ViewABC):
        self._view = view

    def update_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...]):
        self._view.switch_tree('tree_my_balls')

        # Creating ViewModel
        headings = 'Name', 'Due Date'
        widths = 100, 130
        tree_dates = []
        for n, (name, due_date) in enumerate(zip(names, due_dates)):
            d = due_date
            due_date_str = f'{d.year}/{d.month}/{d.day} {d.hour}:{d.minute}'
            tree_dates.append(create_tree_data('', f'{n}', '', (name, due_date_str), (), False))
        stretches = True, False
        scroll_v = True
        scroll_h = True
        view_model = create_view_model_tree(headings, widths, tree_dates, stretches, scroll_v, scroll_h)

        self._view.update_tree(view_model)
