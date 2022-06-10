import abc
import datetime
from typing import Tuple


class PresentersABC(abc.ABC):

    @abc.abstractmethod
    def update_my_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...],
                        select_indexes: Tuple[int, ...] = (), **kwargs):
        pass

    @abc.abstractmethod
    def update_their_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...],
                           select_indexes: Tuple[int, ...] = (), **kwargs):
        pass

    @abc.abstractmethod
    def update_card_name(self, name: str):
        pass

    @abc.abstractmethod
    def update_card_date_created(self, date_created: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_card_due_date(self, due_date: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_card_client(self, client_name: str):
        pass

    @abc.abstractmethod
    def deselect_my_cards(self):
        pass

    @abc.abstractmethod
    def deselect_their_cards(self):
        pass

    @abc.abstractmethod
    def updates_card_actions(self, action_names: Tuple[str, ...], times_expected: Tuple[datetime.timedelta, ...],
                             next_selection_index: int = None, **kwargs):
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
