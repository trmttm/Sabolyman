from Entities import Card
from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from .abc import UseCase


class DuplicateCard(UseCase):
    def __init__(self, entities: EntitiesABC, original_card: Card):
        self._entities = entities
        self._original_card = original_card

    def execute(self):
        clone_card = Card()
        clone_card.load_state(self._original_card.state)
        clone_card.set_id()

        s: SynchronizerABC = self._entities.synchronizer
        for a in clone_card.all_actions:
            a.set_id()
            if s.action_has_implementation_card(a.id):
                DuplicateCard(self._entities, s.get_implementation_card(a.id)).execute()

        clone_card.set_name(f'{clone_card.name} copied')
        clone_card.update_date_created()
        self._entities.add_new_card(clone_card)
        self._entities.set_active_card(clone_card)
