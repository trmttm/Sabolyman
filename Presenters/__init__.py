import datetime
from typing import Tuple

from interface_view import ViewABC

import WidgetNames
from . import update_actions
from . import update_my_cards_list
from . import update_their_cards_list
from .abc import PresentersABC
from .utilities import datetime_to_str
from .utilities import time_delta_to_str


class Presenters(PresentersABC):
    def __init__(self, view: ViewABC):
        self._view = view

    def upon_load_gui(self, view_model: list):
        self._view.add_widgets(view_model)

    def set_up_after_gui(self):
        # This is needed to fix tree columns width.
        self.update_my_cards(('',), (datetime.datetime.today(),), (0,))
        self.update_my_cards((), (), ())

        self.update_their_cards(('',), (datetime.datetime.today(),), (0,))
        self.update_their_cards((), (), ())

    # Card
    def update_my_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...],
                        select_indexes: Tuple[int, ...] = (), **kwargs):
        update_my_cards_list.execute(self._view, due_dates, names, select_indexes, **kwargs)

    def update_their_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...],
                           select_indexes: Tuple[int, ...] = (), **kwargs):
        update_their_cards_list.execute(self._view, due_dates, names, select_indexes, **kwargs)

    def update_card_name(self, name: str):
        self._view.set_value(WidgetNames.entry_card_name, name)

    def update_card_date_created(self, date_created: datetime.datetime):
        self._view.set_value(WidgetNames.label_date_created, datetime_to_str(date_created))

    def update_card_due_date(self, due_date: datetime.datetime):
        self._view.set_value(WidgetNames.entry_dead_line, datetime_to_str(due_date))

    def deselect_my_cards(self):
        self._view.deselect_tree_items(WidgetNames.tree_my_cards)

    def deselect_their_cards(self):
        self._view.deselect_tree_items(WidgetNames.tree_their_cards)

    # Action
    def updates_card_actions(self, action_names: Tuple[str], expected_times: Tuple[datetime.timedelta, ...],
                             next_selection_indexes: Tuple[int, ...] = (), **kwargs):
        update_actions.execute(self._view, expected_times, action_names, next_selection_indexes, **kwargs)

    def update_action_name(self, name: str):
        self._view.set_value(WidgetNames.entry_action_name, name)

    def update_action_date_created(self, date_created: datetime.datetime):
        pass

    def update_action_time_expected(self, time_expected: datetime.timedelta):
        self._view.set_value(WidgetNames.entry_action_time_expected, time_delta_to_str(time_expected))

    def update_action_owner(self, owner_name: str):
        self._view.set_value(WidgetNames.entry_action_owner, owner_name)

    def update_action_is_done(self, is_done: bool):
        self._view.set_value(WidgetNames.check_button_action_done, is_done)

    def update_action_description(self, description: str):
        self._view.set_value(WidgetNames.text_box_action_description, description)

    def update_action_files(self, files_names: Tuple[str, ...]):
        pass
