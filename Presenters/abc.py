import abc
import datetime
from typing import Callable
from typing import Tuple


class PresentersABC(abc.ABC):

    @abc.abstractmethod
    def update_my_cards(self, names: Tuple[str, ...], sort_by: str, sorter_values: Tuple[datetime.datetime, ...],
                        select_indexes: Tuple[int, ...] = (), **kwargs):
        pass

    @abc.abstractmethod
    def update_their_cards(self, names: Tuple[str, ...], sort_by: str, sorter_values: Tuple[datetime.datetime, ...],
                           select_indexes: Tuple[int, ...] = (), **kwargs):
        pass

    @abc.abstractmethod
    def update_card_name(self, name: str):
        pass

    @abc.abstractmethod
    def update_card_importance(self, importance: int):
        pass

    @abc.abstractmethod
    def update_card_date_created(self, date_created: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_card_due_date(self, due_date: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_action_due_date(self, due_date: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_action_start_from(self, due_date: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_action_client(self, client_name: str):
        pass

    @abc.abstractmethod
    def deselect_my_cards(self):
        pass

    @abc.abstractmethod
    def deselect_their_cards(self):
        pass

    @abc.abstractmethod
    def updates_card_actions(self, action_names: tuple, second_column_data: tuple,
                             next_selection_indexes: Tuple[int, ...] = (), **kwargs):
        pass

    @abc.abstractmethod
    def upon_load_gui(self, view_model: list):
        pass

    # Action
    @abc.abstractmethod
    def update_action_name(self, name: str):
        pass

    @abc.abstractmethod
    def update_action_date_created(self, date_created: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_action_time_expected(self, time_expected: datetime.timedelta):
        pass

    @abc.abstractmethod
    def update_action_owner(self, owner_name: str):
        pass

    @abc.abstractmethod
    def update_action_is_done(self, is_done: bool):
        pass

    @abc.abstractmethod
    def update_action_description(self, description: str):
        pass

    @abc.abstractmethod
    def update_action_files(self, files_names: Tuple[str, ...]):
        pass

    @abc.abstractmethod
    def show_mail_creator(self, file_name: str, template_to_text: dict):
        pass

    @abc.abstractmethod
    def show_minutes_setter(self, view_model, upon_ok: Callable = None, **kwargs):
        pass

    @abc.abstractmethod
    def show_datetime_setter(self, view_model, upon_ok: Callable = None, **kwargs):
        pass

    @abc.abstractmethod
    def feed_back_user_by_popup(self, title: str, body: str, width: int, height: int, **kwargs):
        pass

    @abc.abstractmethod
    def open_display_progress_dialogue(self, method_upon_ok=None, **kwargs):
        pass

    @abc.abstractmethod
    def open_display_list_of_actions(self, data: dict, callback: Callable[[tuple], None]):
        pass

    @abc.abstractmethod
    def ask_user_for_entries(self, callback: Callable, **kwargs):
        pass

    @abc.abstractmethod
    def ask_user_to_select_from_a_list(self, display_to_data: dict, callback: Callable):
        pass

    @abc.abstractmethod
    def open_filter_setting(self, commands: dict, states: dict):
        pass

    @abc.abstractmethod
    def ask_user_date(self, upon_date_selected: Callable):
        pass

    @abc.abstractmethod
    def update_action_resources(self, resources: tuple, **kwargs):
        pass
