import abc
import datetime
from typing import Tuple

from .action import Action
from .card import Card
from .person import Person


class EntitiesABC(abc.ABC):
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
    def all_actions(self):
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
    def existing_my_card_names(self) -> Tuple[str, ...]:
        pass

    @property
    @abc.abstractmethod
    def existing_my_card_due_dates(self) -> Tuple[datetime.datetime, ...]:
        pass

    @abc.abstractmethod
    def get_card_by_index(self, index: int) -> Card:
        pass

    @abc.abstractmethod
    def set_active_card(self, card: Card):
        pass

    @property
    @abc.abstractmethod
    def active_card(self) -> Card:
        pass

    @property
    @abc.abstractmethod
    def card_names(self) -> Tuple[str, ...]:
        pass

    @property
    @abc.abstractmethod
    def due_dates(self) -> Tuple[datetime.datetime, ...]:
        pass

    @abc.abstractmethod
    def add_new_card(self, card: Card):
        pass

    @property
    @abc.abstractmethod
    def all_cards(self) -> Tuple[Card, ...]:
        pass

    @abc.abstractmethod
    def remove_card(self, card: Card):
        pass

    @abc.abstractmethod
    def add_new_action(self, action: Action):
        pass
