import datetime
from typing import Callable
from typing import Tuple

import Utilities
from interface_view import ViewABC

import WidgetNames
from . import ask_user_date
from . import display_progress_dialogue
from . import message_box
from . import show_datetime_setter
from . import show_mail_creator
from . import show_minute_setter
from . import update_actions
from . import update_my_cards_list
from . import update_their_cards_list
from .abc import PresentersABC


class Presenters(PresentersABC):
    def __init__(self, view: ViewABC):
        self._view = view

    def upon_load_gui(self, view_model: list):
        self._view.add_widgets(view_model)

    def set_up_after_gui(self):
        # This is needed to fix tree columns width.
        self.update_my_cards(('',), '', (datetime.datetime.today(),), (0,))
        self.update_my_cards((), '', (), ())

        self.update_their_cards(('',), '', (datetime.datetime.today(),), (0,))
        self.update_their_cards((), '', (), ())

    # Card
    def update_my_cards(self, names: Tuple[str, ...], sort_by: str, sorter_values: Tuple[datetime.datetime, ...],
                        select_indexes: Tuple[int, ...] = (), **kwargs):
        update_my_cards_list.execute(self._view, sort_by, sorter_values, names, select_indexes, **kwargs)

    def update_their_cards(self, names: Tuple[str, ...], sort_by: str, sorter_values: Tuple[datetime.datetime, ...],
                           select_indexes: Tuple[int, ...] = (), **kwargs):
        update_their_cards_list.execute(self._view, sort_by, sorter_values, names, select_indexes, **kwargs)

    def update_card_name(self, name: str):
        self._view.set_value(WidgetNames.entry_card_name, name)

    def update_card_importance(self, importance: int):
        self._view.set_value(WidgetNames.entry_card_importance, importance)

    def update_card_date_created(self, date_created: datetime.datetime):
        self._view.set_value(WidgetNames.label_date_created, Utilities.datetime_to_str(date_created))

    def update_card_due_date(self, due_date: datetime.datetime):
        self._view.set_value(WidgetNames.label_card_dead_line, Utilities.datetime_to_str(due_date))

    def update_action_due_date(self, due_date: datetime.datetime):
        self._view.set_value(WidgetNames.entry_action_dead_line, Utilities.datetime_to_str(due_date))

    def update_action_start_from(self, start_from: datetime.datetime):
        self._view.set_value(WidgetNames.entry_action_start_from, Utilities.datetime_to_str(start_from))

    def update_action_client(self, client_name: str):
        self._view.set_value(WidgetNames.entry_action_client, client_name)

    def deselect_my_cards(self):
        self._view.deselect_tree_items(WidgetNames.tree_my_cards)

    def deselect_their_cards(self):
        self._view.deselect_tree_items(WidgetNames.tree_their_cards)

    # Action
    def updates_card_actions(self, action_names: tuple, second_column_data: tuple,
                             next_selection_indexes: Tuple[int, ...] = (), **kwargs):
        update_actions.execute(self._view, second_column_data, action_names, next_selection_indexes, **kwargs)

    def update_action_name(self, name: str):
        self._view.set_value(WidgetNames.entry_action_name, name)

    def update_action_date_created(self, date_created: datetime.datetime):
        pass

    def update_action_time_expected(self, time_expected: datetime.timedelta):
        self._view.set_value(WidgetNames.entry_action_time_expected, str(time_expected))

    def update_action_owner(self, owner_name: str):
        self._view.set_value(WidgetNames.entry_action_owner, owner_name)

    def update_action_is_done(self, is_done: bool):
        self._view.set_value(WidgetNames.check_button_action_done, is_done)

    def update_action_description(self, description: str):
        self._view.set_value(WidgetNames.text_box_action_description, description)

    def update_action_files(self, files_names: Tuple[str, ...]):
        pass

    def show_mail_creator(self, file_name: str, template_to_text: dict):
        show_mail_creator.execute(self._view, file_name, template_to_text)

    def show_minutes_setter(self, view_model, upon_ok: Callable = None,**kwargs):
        show_minute_setter.execute(self._view, view_model, upon_ok, **kwargs)

    def show_datetime_setter(self, view_model, upon_ok: Callable = None, **kwargs):
        show_datetime_setter.execute(self._view, view_model, upon_ok, **kwargs)

    # Popup
    def feed_back_user_by_popup(self, title: str, body: str, width: int, height: int, **kwargs):
        message_box.execute(self._view, title, body, width, height, **kwargs)

    def open_display_progress_dialogue(self, method_upon_ok=None, **kwargs):
        display_progress_dialogue.execute(self._view, method_upon_ok, **kwargs)

    def ask_user_date(self, upon_date_selected: Callable):
        ask_user_date.execute(self._view, upon_date_selected)

    # Search box
    def set_search_box(self, text: str):
        self._view.set_value(WidgetNames.entry_search_box, text)

    def set_search_mode(self, filter_mode: str):
        self._view.set_value(WidgetNames.combobox_search_mode, filter_mode)
