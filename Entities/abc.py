import abc
import datetime
from typing import Tuple

from .cards import Cards
from .person import Person


class EntitiesABC(abc.ABC):
    @property
    @abc.abstractmethod
    def default_card_name(self) -> str:
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
    def cards(self) -> Cards:
        pass

    @property
    @abc.abstractmethod
    def existing_my_card_names(self) -> Tuple[str, ...]:
        pass

    @property
    @abc.abstractmethod
    def existing_my_card_due_dates(self) -> Tuple[datetime.datetime, ...]:
        pass

    @property
    @abc.abstractmethod
    def card_names(self) -> Tuple[str, ...]:
        pass

    @property
    @abc.abstractmethod
    def due_dates(self) -> Tuple[datetime.datetime, ...]:
        pass
