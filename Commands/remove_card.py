from typing import Iterable
from typing import Tuple

from Entities import Card
from Entities import EntitiesABC

from .abc import UseCase


class RemoveCard(UseCase):
    def __init__(self, entities: EntitiesABC, indexes: Iterable, cards: Tuple[Card, ...]):
        self._entities = entities
        self._indexes = indexes
        self._cards = cards

    def execute(self):
        entities = self._entities
        cards = self._cards
        cards_to_remove = [c for (n, c) in enumerate(cards) if n in self._indexes]
        for card in cards_to_remove:
            entities.remove_card(card)
