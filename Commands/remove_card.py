from typing import Iterable

from Entities import EntitiesABC
from .abc import UseCase


class RemoveCard(UseCase):
    def __init__(self, entities: EntitiesABC, indexes: Iterable):
        self._entities = entities
        self._indexes = indexes

    def execute(self):
        entities = self._entities
        cards = entities.all_cards
        cards_to_remove = [c for (n, c) in enumerate(cards) if n in self._indexes]
        for card in cards_to_remove:
            entities.remove_card(card)
