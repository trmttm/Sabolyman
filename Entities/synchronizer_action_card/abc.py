import abc
from typing import Union

from Entities.action import Action
from Entities.card import Card


class SynchronizerABC(abc.ABC):
    @abc.abstractmethod
    def get_implementation_card(self, action_id: str) -> Union[Card, None]:
        pass

    @abc.abstractmethod
    def get_policy_action(self, card_id: str) -> Union[Action, None]:
        pass

    @abc.abstractmethod
    def deregister_by_action(self, action_id):
        pass

    @abc.abstractmethod
    def deregister_by_card(self, card_id):
        pass

    @abc.abstractmethod
    def notify(self, **kwargs):
        pass

    @abc.abstractmethod
    def action_has_implementation_card(self, action_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_all_descendants(self, parent_card: Card) -> list[Card]:
        pass

    @abc.abstractmethod
    def get_immediate_parents(self, child_card: Card) -> list[Card]:
        pass

    @abc.abstractmethod
    def card_has_policy_action(self, card_id: str) -> bool:
        pass

    @property
    @abc.abstractmethod
    def state(self) -> dict:
        pass

    def synchronize_card_to_action(self, policy_action: Action, implementation_card: Card):
        pass
