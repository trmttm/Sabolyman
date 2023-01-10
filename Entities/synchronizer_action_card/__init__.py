from typing import Dict

from .mutual_sync import synchronize_mutually
from ..abc_entities import EntitiesABC
from ..abc_entity import EntityABC
from ..action import Action
from ..card import Card


class SynchronizerActionCard(EntityABC):
    def __init__(self, entities: EntitiesABC):
        self._entities = entities
        self._synchronization_table: Dict[str, str] = {}

    def synchronize(self, action_policy: Action, card_implementation: Card):
        # Register
        action_policy.set_id()
        card_implementation.set_id()
        self.register(action_policy.id, card_implementation.id)

        # initial synchronization
        card_implementation.set_name(action_policy.name)
        card_implementation.set_color(action_policy.color)

        synchronize_mutually(action_policy, card_implementation)

    def register(self, action_id, card_id):
        self._synchronization_table[action_id] = card_id

    def deregister_by_action(self, action_id):
        if action_id in tuple(self._synchronization_table.keys()):
            del self._synchronization_table[action_id]

    def deregister_by_card(self, card_id):
        for action_id in tuple(self._synchronization_table.keys()):
            if self._synchronization_table.get(action_id) == card_id:
                del self._synchronization_table[action_id]

    def load_state(self, state: dict):
        self._synchronization_table = state.get('sync_state', {})

        for action_id in tuple(self._synchronization_table.keys()):
            card_id = self._synchronization_table.get(action_id)

            action = self._entities.get_action_by_id(action_id)
            card = self._entities.get_card_by_id(card_id)
            if action is None:
                self.deregister_by_action(action_id)
            elif card is None:
                self.deregister_by_card(card_id)
            else:
                synchronize_mutually(action, card)

    @property
    def state(self) -> dict:
        return {'sync_state': self._synchronization_table, }
