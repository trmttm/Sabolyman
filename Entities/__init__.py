import datetime
from typing import Tuple

from .abc import EntitiesABC
from .card import Card
from .cards import Cards
from .file import File
from .files import Files
from .person import Person


class Entities(EntitiesABC):
    @property
    def due_dates(self) -> Tuple[datetime.datetime, ...]:
        return self._cards.due_dates

    @property
    def card_names(self) -> Tuple[str, ...]:
        return self._cards.card_names

    @property
    def existing_my_card_due_dates(self) -> Tuple[datetime.datetime, ...]:
        return datetime.datetime(2022, 6, 2), datetime.datetime(2022, 5, 31)

    @property
    def existing_my_card_names(self) -> Tuple[str, ...]:
        return 'Card1', 'Card2',

    def __init__(self):
        self._cards = Cards()

    @property
    def default_card_name(self) -> str:
        return '新たなカード'

    @property
    def user(self) -> Person:
        return Person('山家太郎')

    @property
    def default_importance(self) -> int:
        return 5

    @property
    def default_dead_line(self) -> datetime.datetime:
        return datetime.datetime.today()

    @property
    def cards(self) -> Cards:
        return self._cards
