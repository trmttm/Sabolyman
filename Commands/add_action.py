from Entities import Action
from Entities import EntitiesABC
from .abc import UseCase


class AddAction(UseCase):
    def __init__(self, entities: EntitiesABC):
        self._entities = entities

    def execute(self):
        entities = self._entities

        name = entities.default_action_name
        owner = entities.user
        time_expected = entities.default_action_time_expected

        action = Action()
        action.set_name(name)
        action.set_owner(owner)
        action.set_time_expected(time_expected)

        entities.add_new_action(action)
