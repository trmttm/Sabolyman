import datetime
from typing import Tuple

from interface_view import ViewABC

import WidgetNames
from . import update_actions
from . import update_cards
from .abc import PresentersABC
from .utilities import datetime_to_str
from .utilities import datetime_to_str


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
        update_cards.execute(self._view, due_dates, names, select_nth)

    def update_card_name(self, name: str):
        self._view.set_value(WidgetNames.entry_card_name, name)

    def update_card_date_created(self, date_created: datetime.datetime):
        self._view.set_value(WidgetNames.label_date_created, datetime_to_str(date_created))

    def update_card_due_date(self, due_date: datetime.datetime):
        self._view.set_value(WidgetNames.entry_dead_line, datetime_to_str(due_date))

    def updates_card_actions(self, action_names: Tuple[str], times_expected: Tuple[datetime.timedelta, ...],
                             next_selection_index: int = None):
        update_actions.execute(self._view, times_expected, action_names, next_selection_index)
