import datetime
from typing import List
from typing import Tuple

from .abc import EntitiesABC
from .action import Action
from .card import Card
from .cards import Cards
from .file import File
from .files import Files
from .person import Person


class Entities(EntitiesABC):
    def set_active_card(self, card: Card):
        self._cards.set_active_card(card)

    @property
    def active_card(self) -> Card:
        return self._cards.active_card

    def get_card_by_index(self, index: int) -> Card:
        return self._cards.get_card_by_index(index)

    def remove_card(self, card: Card):
        self._cards.remove_card(card)

    @property
    def all_cards(self) -> List[Card]:
        return self._cards.all_cards

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
        return f'新たなカード {self._cards.nth}'

    @property
    def user(self) -> Person:
        return Person('山家太郎')

    @property
    def default_importance(self) -> int:
        return 5

    @property
    def default_dead_line(self) -> datetime.datetime:
        return datetime.datetime.today()

    def add_new_card(self, card: Card):
        return self._cards.add_new_card(card)
