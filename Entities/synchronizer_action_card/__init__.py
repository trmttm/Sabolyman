from typing import Callable
from typing import Dict
from typing import Union

from . import constants
from .abc import SynchronizerABC
from .sync_add_new_action import synchronize_add_new_action
from .sync_dead_line import sync_dead_line
from .sync_mark_done import sync_mark_done
from .sync_mutually import sync_mutually
from .sync_remove_action import synchronize_remove_action
from ..abc_entities import EntitiesABC
from ..abc_entity import EntityABC
from ..action import Action
from ..card import Card


class SynchronizerActionCard(EntityABC, SynchronizerABC):
    def __init__(self, entities: EntitiesABC):
        self._entities = entities
        self._synchronization_table: Dict[str, str] = {}
        self._subscribers = []

        synchronize_remove_action(entities, self)
        synchronize_add_new_action(self._entities, self)

    def synchronize(self, policy_action: Action, implementation_card: Card):
        # Register
        policy_action.set_id()
        implementation_card.set_id()
        self.register(policy_action.id, implementation_card.id)

        # initial synchronization
        implementation_card.set_name(policy_action.name)
        implementation_card.set_color(policy_action.color)

        synchronize(implementation_card, policy_action, self)

    def attach_to_notification(self, method: Callable):
        self._subscribers.append(method)

    def notify(self, **kwargs):
        for method in self._subscribers:
            method(**kwargs)

    def register(self, action_id, card_id):
        self._synchronization_table[action_id] = card_id

    def deregister_by_action(self, action_id):
        if action_id in tuple(self._synchronization_table.keys()):
            del self._synchronization_table[action_id]

    def deregister_by_card(self, card_id):
        for action_id in tuple(self._synchronization_table.keys()):
            if self.get_implementation_card_id(action_id) == card_id:
                del self._synchronization_table[action_id]

    def action_has_implementation_card(self, action_id: str) -> bool:
        return action_id in self._synchronization_table

    def card_has_policy_action(self, card_id: str) -> bool:
        return card_id in self._synchronization_table.values()

    def get_implementation_card_id(self, action_id):
        return self._synchronization_table.get(action_id)

    def get_implementation_card(self, action_id: str) -> Union[Card, None]:
        return self._entities.get_card_by_id(self.get_implementation_card_id(action_id))

    def get_policy_action_id(self, card_id: str) -> Union[Action, str]:
        for action_id, c_id in self._synchronization_table.items():
            if card_id == c_id:
                return action_id

    def get_policy_action(self, card_id: str) -> Union[Action, None]:
        action_id = self.get_policy_action_id(card_id)
        if action_id is not None:
            return self._entities.get_action_by_id(action_id)

    def load_state(self, state: dict):
        self._synchronization_table = state.get('sync_state', {})

        for action_id in tuple(self._synchronization_table.keys()):
            card_id = self.get_implementation_card_id(action_id)

            policy_action = self._entities.get_action_by_id(action_id)
            implementation_card = self._entities.get_card_by_id(card_id)
            if policy_action is None:  # clean up state
                self.deregister_by_action(action_id)
            elif implementation_card is None:  # clean up state
                self.deregister_by_card(card_id)
            else:
                synchronize(implementation_card, policy_action, self)

    @property
    def state(self) -> dict:
        return {'sync_state': self._synchronization_table, }


def synchronize(implementation_card: Card, policy_action: Action, synchronizer: SynchronizerABC):
    sync_mutually(policy_action, implementation_card, synchronizer)
    sync_dead_line(policy_action, synchronizer.get_implementation_card)
    sync_mark_done(implementation_card, synchronizer.get_policy_action)
