from Entities import EntitiesABC
from .abc import UseCase
from .create_action import CreateAction


class AddAction(UseCase):
    def __init__(self, entities: EntitiesABC):
        self._command_create_action = CreateAction(entities)
        self._entities = entities

    def execute(self):
        entities = self._entities

        action = self._command_create_action.execute()
        action.set_color(entities.active_card.color)
        entities.add_new_action(action)
        entities.set_active_action(action)
