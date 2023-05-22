from Entities import Card
from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC

from .abc import UseCase


class DuplicateCard(UseCase):
    def __init__(self, entities: EntitiesABC, original_card: Card):
        self._entities = entities
        self._original_card = original_card

    def execute(self) -> Card:
        clone_card = Card()
        clone_card.load_state(self._original_card.state)
        self._entities.force_set_ids(clone_card)

        s: SynchronizerABC = self._entities.synchronizer
        for clone_action, original_action in zip(clone_card.all_actions, self._original_card.all_actions):
            if s.action_has_implementation_card(original_action.id):
                # Recursively clone
                impl_card = DuplicateCard(self._entities, s.get_implementation_card(original_action.id)).execute()
                self._entities.synchronize_action_to_card(clone_action, impl_card)

        clone_card.set_name(f'{clone_card.name} copied')
        clone_card.update_date_created()
        self._entities.add_new_card(clone_card)
        self._entities.set_active_card(clone_card)

        return clone_card
