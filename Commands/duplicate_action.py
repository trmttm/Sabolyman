from Entities import Action
from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from .abc import UseCase
from .duplicate_card import DuplicateCard


class DuplicateAction(UseCase):
    def __init__(self, entities: EntitiesABC, original_action: Action):
        self._entities = entities
        self._original_action = original_action

    def execute(self):
        initial_active_card = self._entities.active_card
        original_action = self._original_action

        clone_action = Action()
        clone_action.load_state(original_action.state)
        clone_action.force_set_id()
        clone_action.set_name(f'{clone_action.name} copied')
        clone_action.update_date_created()

        s: SynchronizerABC = self._entities.synchronizer
        if s.action_has_implementation_card(original_action.id):
            implementation_card = s.get_implementation_card(original_action.id)
            clone_implementation_card = DuplicateCard(self._entities, implementation_card).execute()
            s.synchronize_card_to_action(clone_action, clone_implementation_card)

        self._entities.set_active_card(initial_active_card)
        self._entities.add_new_action(clone_action)
        self._entities.set_active_action(clone_action)
