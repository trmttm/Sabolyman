from Entities import Card
from Entities import EntitiesABC

from .abc import UseCase


class AddCard(UseCase):
    def __init__(self, entities: EntitiesABC):
        self._entities = entities

    def execute(self):
        entities = self._entities

        name = entities.default_card_name
        owner = entities.user
        importance = entities.default_importance

        card = Card()
        card.set_name(name)
        card.set_owner(owner)
        card.set_importance(importance)

        entities.add_new_card(card)
        entities.set_active_card(card)
