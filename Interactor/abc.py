import abc
from typing import Tuple

from interface_keymaps import KeyMapsABC


class InteractorABC(abc.ABC):
    @abc.abstractmethod
    def save_to_file(self, file_name: str):
        pass

    @abc.abstractmethod
    def load_state_from_file(self, file_name: str):
        pass

    @abc.abstractmethod
    def save_as_template_card(self, file_name: str):
        pass

    @abc.abstractmethod
    def add_template_card(self, file_name: str):
        pass

    @abc.abstractmethod
    def add_new_card(self):
        pass

    @abc.abstractmethod
    def delete_selected_my_cards(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def delete_selected_their_cards(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def show_my_card_information(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def show_their_card_information(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def set_card_name(self, card_name: str):
        pass

    @abc.abstractmethod
    def set_dead_line(self, dead_line_str: str):
        pass

    @abc.abstractmethod
    def set_client(self, dead_line_str: str):
        pass

    @abc.abstractmethod
    def add_new_action(self):
        pass

    @abc.abstractmethod
    def delete_selected_actions(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def show_action_information(self, indexes: Tuple[int]):
        pass

    @abc.abstractmethod
    def set_action_name(self, action_name: str):
        pass

    @abc.abstractmethod
    def set_action_owner(self, owner_name: str):
        pass

    @abc.abstractmethod
    def mark_action_completed(self, done_or_not: bool):
        pass

    @abc.abstractmethod
    def set_action_complete_time(self, done_or_not: bool):
        pass

    @abc.abstractmethod
    def set_action_description(self, description: str):
        pass

    @abc.abstractmethod
    def set_action_time_expected(self, time_expected: str):
        pass

    @abc.abstractmethod
    def move_my_cards_up(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def move_my_cards_down(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def move_their_cards_up(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def move_their_cards_down(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def move_actions_up(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def move_actions_down(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def duplicate_selected_card(self):
        pass

    @abc.abstractmethod
    def set_active_keymap(self, name: str):
        pass

    @abc.abstractmethod
    def add_new_keyboard_shortcut(self, key_combo: tuple, command_and_feedback: tuple):
        pass

    @property
    @abc.abstractmethod
    def keymaps(self) -> KeyMapsABC:
        pass

    @abc.abstractmethod
    def close(self, command):
        pass

    @abc.abstractmethod
    def set_color_to_cards(self, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...], color):
        pass

    @property
    @abc.abstractmethod
    def mail_template_path(self) -> str:
        pass

    @abc.abstractmethod
    def make_email(self):
        pass

    @abc.abstractmethod
    def hide_finished_cards(self):
        pass

    @abc.abstractmethod
    def unhide_finished_cards(self):
        pass
