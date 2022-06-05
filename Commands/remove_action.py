from typing import Iterable

from Entities import EntitiesABC
from .abc import UseCase


class RemoveAction(UseCase):
    def __init__(self, entities: EntitiesABC, indexes: Iterable):
        self._entities = entities
        self._indexes = indexes

    def execute(self):
        entities = self._entities
        actions = entities.all_actions
        actions_to_remove = [a for (n, a) in enumerate(actions) if n in self._indexes]
        for action in actions_to_remove:
            entities.remove_action(action)
