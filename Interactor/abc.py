import abc
from typing import Tuple


class InteractorABC(abc.ABC):
    @abc.abstractmethod
    def add_new_card(self):
        pass

    @abc.abstractmethod
    def delete_selected_cards(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def show_card_information(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def set_card_name(self, card_name: str):
        pass

    @abc.abstractmethod
    def set_dead_line(self, dead_line_str: str):
        pass

    @abc.abstractmethod
    def add_new_action(self):
        pass
