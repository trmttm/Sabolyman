from Entities import Action
from Entities import EntitiesABC
from .abc import UseCase


class DuplicateAction(UseCase):
    def __init__(self, entities: EntitiesABC, original_action: Action):
        self._entities = entities
        self._original_action = original_action

    def execute(self):
        clone_action = Action()
        clone_action.load_state(self._original_action.state)
        clone_action.set_name(f'{clone_action.name} copied')
        clone_action.update_date_created()
        self._entities.add_new_action(clone_action)
        self._entities.set_active_action(clone_action)
