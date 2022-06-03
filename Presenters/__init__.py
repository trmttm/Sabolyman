import datetime
from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC

from .abc import PresentersABC


def datetime_to_str(d):
    due_date_str = f'{d.year}/{d.month}/{d.day} {d.hour}:{d.minute}'
    return due_date_str


class Presenters(PresentersABC):
    def __init__(self, view: ViewABC):
        self._view = view

    def update_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...], select_nth: int = None):
        self._view.switch_tree('tree_my_balls')

        # Creating ViewModel
        headings = 'Name', 'Due Date'
        widths = 100, 130
        tree_dates = []
        for n, (name, due_date) in enumerate(zip(names, due_dates)):
            d = due_date
            due_date_str = datetime_to_str(d)
            tree_dates.append(create_tree_data('', f'{n}', '', (name, due_date_str), (), n == select_nth))
        stretches = True, False
        scroll_v = True
        scroll_h = True
        view_model = create_view_model_tree(headings, widths, tree_dates, stretches, scroll_v, scroll_h)

        self._view.update_tree(view_model)

    def update_card_name(self, name: str):
        self._view.set_value('entry_name', name)

    def update_card_date_created(self, date_created: datetime.datetime):
        self._view.set_value('lbl_date_created2', datetime_to_str(date_created))

    def update_card_due_date(self, due_date: datetime.datetime):
        self._view.set_value('entry_dead_line', datetime_to_str(due_date))

    def updates_card_actions(self):
        pass
