import datetime
from typing import List
from typing import Tuple

from .card import Card


class Cards:
    def __init__(self):
        self._cards: List[Card, ...] = []
        self._id = 0
        self._active_card = None

    @property
    def active_card(self) -> Card:
        return self._active_card

    def set_active_card(self, card: Card):
        self._active_card = card

    def add_new_card(self, card: Card):
        self._cards.append(card)

    def get_card_by_index(self, index: int) -> Card:
        try:
            return self._cards[index]
        except IndexError:
            pass

    @property
    def card_names(self) -> Tuple[str, ...]:
        return tuple(c.name for c in self._cards)

    @property
    def due_dates(self) -> Tuple[datetime.datetime, ...]:
        return tuple(c.due_date for c in self._cards)

    @property
    def all_cards(self) -> List[Card]:
        return self._cards

    def remove_card(self, card: Card):
        self._cards.remove(card)

    @property
    def nth(self) -> int:
        self._id += 1
        return self._id
