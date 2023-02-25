import abc
import datetime
from typing import Callable
from typing import Tuple
from typing import Union

from .action import Action
from .card import Card
from .person import Person


class EntitiesABC(abc.ABC):

    @property
    @abc.abstractmethod
    def my_cards(self) -> Tuple[Card, ...]:
        pass

    @property
    @abc.abstractmethod
    def their_cards(self) -> Tuple[Card, ...]:
        pass

    @property
    @abc.abstractmethod
    def all_cards(self) -> Tuple[Card, ...]:
        pass

    @property
    @abc.abstractmethod
    def all_actions(self) -> Tuple[Action, ...]:
        pass

    @property
    @abc.abstractmethod
    def my_visible_cards(self) -> Tuple[Card, ...]:
        pass

    @property
    @abc.abstractmethod
    def their_visible_cards(self) -> Tuple[Card, ...]:
        pass

    @property
    @abc.abstractmethod
    def default_card_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def default_action_time_expected(self) -> datetime.timedelta:
        pass

    @property
    @abc.abstractmethod
    def default_action_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def action_names(self) -> Tuple[str, ...]:
        pass

    @property
    @abc.abstractmethod
    def times_expected(self) -> Tuple[datetime.timedelta, ...]:
        pass

    @property
    @abc.abstractmethod
    def times_completed(self) -> Tuple[datetime.datetime, ...]:
        pass

    @property
    @abc.abstractmethod
    def user(self) -> Person:
        pass

    @property
    @abc.abstractmethod
    def default_importance(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def default_dead_line(self) -> datetime.datetime:
        pass

    @property
    @abc.abstractmethod
    def default_start_from(self) -> datetime.datetime:
        pass

    @property
    @abc.abstractmethod
    def default_client_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_my_card_by_index(self, index: int) -> Card:
        pass

    @abc.abstractmethod
    def get_their_card_by_index(self, index: int) -> Card:
        pass

    @abc.abstractmethod
    def get_my_visible_cards_by_indexes(self, indexes: Tuple[int, ...]) -> Tuple[Card, ...]:
        pass

    @abc.abstractmethod
    def get_their_visible_cards_by_indexes(self, indexes: Tuple[int, ...]) -> Tuple[Card, ...]:
        pass

    @abc.abstractmethod
    def set_active_card(self, card: Card):
        pass

    @property
    @abc.abstractmethod
    def active_card(self) -> Card:
        pass

    @abc.abstractmethod
    def add_new_card(self, card: Card):
        pass

    @abc.abstractmethod
    def remove_card(self, card: Card):
        pass

    @abc.abstractmethod
    def add_new_action(self, action: Action):
        pass

    @abc.abstractmethod
    def remove_action(self, action: Action):
        pass

    @abc.abstractmethod
    def get_action_by_index(self, index: int) -> Action:
        pass

    @abc.abstractmethod
    def set_active_action(self, actions: Action):
        pass

    @property
    @abc.abstractmethod
    def active_action(self) -> Action:
        pass

    @property
    @abc.abstractmethod
    def state(self) -> dict:
        pass

    @abc.abstractmethod
    def create_new_person(self, name: str):
        pass

    @abc.abstractmethod
    def load_state(self, state: dict):
        pass

    @abc.abstractmethod
    def move_my_cards_up(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        pass

    @abc.abstractmethod
    def move_my_cards_down(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        pass

    @abc.abstractmethod
    def move_their_cards_up(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        pass

    @abc.abstractmethod
    def move_their_cards_down(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        pass

    @abc.abstractmethod
    def move_actions_up(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        pass

    @abc.abstractmethod
    def move_actions_down(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        pass

    @property
    @abc.abstractmethod
    def active_card_is_in_my_cards(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def active_card_is_in_their_cards(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def active_action_index(self) -> int:
        pass

    @abc.abstractmethod
    def get_action_index(self, card_: Card, action_: Action):
        pass

    @property
    @abc.abstractmethod
    def selected_actions_indexes(self) -> Tuple[int, ...]:
        pass

    @property
    @abc.abstractmethod
    def selected_actions(self) -> Tuple[Action, ...]:
        pass

    @abc.abstractmethod
    def copy_actions(self, actions_passed: Tuple[Action, ...]):
        pass

    @property
    @abc.abstractmethod
    def copied_actions(self) -> Tuple[Action, ...]:
        pass

    @abc.abstractmethod
    def turn_off_cut_mode(self):
        pass

    @abc.abstractmethod
    def turn_on_cut_mode(self):
        pass

    @property
    @abc.abstractmethod
    def is_cut_mode(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def card_to_cut_action_from(self) -> Card:
        pass

    @property
    @abc.abstractmethod
    def active_card_index(self) -> int:
        pass

    @abc.abstractmethod
    def set_show_this_card(self, card: Card):
        pass

    @property
    @abc.abstractmethod
    def show_this_card(self) -> Union[None, Card]:
        pass

    @abc.abstractmethod
    def clear_show_this_card(self):
        pass

    @abc.abstractmethod
    def hide_finished_cards(self):
        pass

    @abc.abstractmethod
    def unhide_finished_cards(self):
        pass

    @abc.abstractmethod
    def toggle_hide_finished_cards(self):
        pass

    @abc.abstractmethod
    def set_filter_key(self, search_key: str, search_mode: str):
        pass

    @property
    @abc.abstractmethod
    def filter_key(self) -> str:
        pass

    @abc.abstractmethod
    def set_filter_due_date(self, date: datetime.datetime.day):
        pass

    @abc.abstractmethod
    def clear_filter_due_date(self):
        pass

    @property
    @abc.abstractmethod
    def filter_mode(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def all_filter_modes(self) -> Tuple[str, ...]:
        pass

    @abc.abstractmethod
    def clear_filter_key(self):
        pass

    @abc.abstractmethod
    def clear_filter_mode(self):
        pass

    @property
    @abc.abstractmethod
    def sort_by(self) -> str:
        pass

    @abc.abstractmethod
    def sorter_values(self, cards_: Tuple[Card, ...]) -> Tuple[str, ...]:
        pass

    @abc.abstractmethod
    def sort_cards_by_deadline(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_name(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_current_owner(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_current_client(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_importance(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_color(self):
        pass

    @abc.abstractmethod
    def get_action_by_id(self, action_id: str) -> Action:
        pass

    @abc.abstractmethod
    def get_card_by_id(self, card_id: str) -> Card:
        pass

    @abc.abstractmethod
    def get_policy_action(self, card_id: str) -> Union[Action, None]:
        pass

    @abc.abstractmethod
    def get_cards_that_have_action(self, action_: Action) -> Tuple[Card, ...]:
        pass

    @abc.abstractmethod
    def get_implementation_card(self, action_id: str) -> Union[Card, None]:
        pass

    @abc.abstractmethod
    def synchronize_action_to_card(self, action_policy: Action, card_implementation: Card):
        pass

    @abc.abstractmethod
    def synchronize_card_to_action(self, action_policy, card_implementation):
        pass

    @abc.abstractmethod
    def attach_to_synchronizer(self, method: Callable):
        pass

    @property
    @abc.abstractmethod
    def synchronizer(self):
        pass
