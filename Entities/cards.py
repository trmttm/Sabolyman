import datetime
from typing import List
from typing import Tuple

from .card import Card


class Cards:
    def __init__(self):
        self._cards: List[Card, ...] = []

    def add_new_card(self, card: Card):
        self._cards.append(card)

    @property
    def card_names(self) -> Tuple[str, ...]:
        return tuple(c.name for c in self._cards)

    @property
    def due_dates(self) -> Tuple[datetime.datetime, ...]:
        return tuple(c.due_date for c in self._cards)
