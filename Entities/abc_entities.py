import abc
import datetime
from typing import Tuple

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

    @property
    @abc.abstractmethod
    def selected_actions_indexes(self) -> Tuple[int, ...]:
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
    def show_this_card(self):
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
    def set_filter_key(self, search_key: str):
        pass

    @abc.abstractmethod
    def clear_filter_key(self):
        pass
