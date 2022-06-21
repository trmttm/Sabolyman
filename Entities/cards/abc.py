import abc
from typing import List

from Entities.abc_entity import EntityABC
from Entities.card import Card


class CardsABC(EntityABC):
    @property
    @abc.abstractmethod
    def all_cards(self) -> List[Card]:
        pass

    @property
    @abc.abstractmethod
    def active_card(self):
        pass

    @abc.abstractmethod
    def add_new_card(self, card):
        pass

    @abc.abstractmethod
    def set_active_card(self, card):
        pass

    @abc.abstractmethod
    def load_state(self, state: dict):
        pass

    @property
    @abc.abstractmethod
    def hide_finished_cards(self) -> bool:
        pass

    @abc.abstractmethod
    def set_hide_finished_cards(self, true_false: bool):
        pass
