import abc
from typing import Tuple

from interface_keymaps import KeyMapsABC


class InteractorABC(abc.ABC):
    @abc.abstractmethod
    def save_state(self):
        pass

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
    def set_dead_line(self, dead_line_str: str, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def set_client(self, client_name: str, actions_indexes: Tuple[int, ...]):
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
    def set_action_name(self, action_name: str, actions_indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def set_action_owner(self, owner_name: str, actions_indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def mark_action_completed(self, done_or_not: bool, actions_indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def set_action_description(self, description: str, actions_indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def set_action_time_expected(self, time_expected: str, actions_indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def move_my_cards_up(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def move_my_cards_down(self, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def increment_importance(self, increment: int):
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

    @abc.abstractmethod
    def set_color_to_actions(self, indexes: Tuple[int, ...], color):
        pass

    @abc.abstractmethod
    def convert_selected_cards_to_actions(self, left_indexes_and_right_indexes: Tuple[Tuple[int, ...], ...]):
        pass

    @property
    @abc.abstractmethod
    def mail_template_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def state_folder(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def home_folder(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def cards_template_path(self) -> str:
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

    @abc.abstractmethod
    def toggle_hide_finished_cards(self):
        pass

    @abc.abstractmethod
    def filter_cards_by_due_date(self):
        pass

    @abc.abstractmethod
    def clear_filter_due_date(self):
        pass

    @abc.abstractmethod
    def filter_cards_with_keyword(self, keyword: str, search_mode: str):
        pass

    @abc.abstractmethod
    def clear_card_filter(self):
        pass

    @abc.abstractmethod
    def export_actions_list(self, file_name: str):
        pass

    @property
    @abc.abstractmethod
    def search_mode(self) -> Tuple[str, ...]:
        pass

    @abc.abstractmethod
    def show_minutes_setter(self, indexes):
        pass

    @abc.abstractmethod
    def sort_cards_by_color(self):
        pass

    @abc.abstractmethod
    def sort_by_importance(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_deadline(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_name(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_current_owner(self):
        pass

    @abc.abstractmethod
    def sort_cards_by_current_client(self):
        pass

    @abc.abstractmethod
    def shift_actions_dead_lines_by(self, days: int, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def shift_actions_dead_lines_hours_by(self, hours: int, indexes: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def shift_cards_dead_lines_by(self, days: int, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def copy_actions(self):
        pass

    @abc.abstractmethod
    def paste_actions_as_duplicate(self):
        pass

    @abc.abstractmethod
    def paste_actions_as_alias(self):
        pass

    @abc.abstractmethod
    def open_display_progress_dialogue(self):
        pass

    @abc.abstractmethod
    def open_display_new_tasks_dialogue(self):
        pass

    @abc.abstractmethod
    def open_display_due_tasks_dialogue(self):
        pass

    @abc.abstractmethod
    def reset_card_starting_date(self, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...]):
        pass

    @abc.abstractmethod
    def abstract_out_card_as_an_action_and_copy(self):
        pass

    @abc.abstractmethod
    def implement_lower_level_detail(self):
        pass

    @abc.abstractmethod
    def jump_to_implementation_card(self, callback):
        pass

    @abc.abstractmethod
    def jump_to_policy_action(self, callback):
        pass

    @abc.abstractmethod
    def display_selected_card_as_a_graph_on_the_browser(self):
        pass
