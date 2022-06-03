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
        dead_line = entities.default_dead_line

        card = Card()
        card.set_name(name)
        card.set_owner(owner)
        card.set_importance(importance)
        card.set_dead_line(dead_line)
        card.mark_done()

        entities.add_new_card(card)
