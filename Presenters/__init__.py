import datetime
from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC

import WidgetNames
from .abc import PresentersABC


def datetime_to_str(d):
    due_date_str = f'{d.year}/{d.month}/{d.day} {d.hour}:{d.minute}'
    return due_date_str


class Presenters(PresentersABC):
    def load_gui(self, view_model: list):
        self._view.add_widgets(view_model)

    def __init__(self, view: ViewABC):
        self._view = view

    def set_up_after_gui(self):
        # This is needed to fix tree columns width.
        self.update_cards(('',), (datetime.datetime.today(),), 0)
        self.update_cards((), ())

    def update_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...], select_nth: int = None):
        self._view.switch_tree(WidgetNames.tree_my_cards)

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
        self._view.set_value(WidgetNames.entry_card_name, name)

    def update_card_date_created(self, date_created: datetime.datetime):
        self._view.set_value(WidgetNames.label_date_created, datetime_to_str(date_created))

    def update_card_due_date(self, due_date: datetime.datetime):
        self._view.set_value(WidgetNames.entry_dead_line, datetime_to_str(due_date))

    def updates_card_actions(self):
        pass
