from Entities import Card
from Entities import EntitiesABC
from .abc import UseCase


class DuplicateCard(UseCase):
    def __init__(self, entities: EntitiesABC, original_card: Card):
        self._entities = entities
        self._original_card = original_card

    def execute(self):
        clone_card = Card()
        clone_card.load_state(self._original_card.state)
        self._entities.add_new_card(clone_card)
