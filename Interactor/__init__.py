import datetime
import os
from typing import Callable
from typing import Tuple

import Utilities
import os_identifier
from Entities import EntitiesABC
from Entities.priority import Priority
from Gateway.abc import GatewayABC
from Presenters import PresentersABC
from keyboard_shortcut import KeyMaps

from . import abstract_out
from . import add_action_resources
from . import add_new_action
from . import add_new_card
from . import add_new_card_from_templates
from . import clear_filter_by_priority
from . import convert_cards_to_actions
from . import create_mail_menu
from . import delete_selected_actions
from . import delete_selected_my_cards
from . import delete_selected_their_cards
from . import display_due_tasks
from . import display_due_tasks_my_ball
from . import display_due_tasks_their_ball
from . import display_list_of_actions
from . import display_new_tasks
from . import display_progress
from . import draw_graph_on_browser
from . import duplicate_selected_card
from . import export_actions_list
from . import export_gantt_chart_data
from . import filter_by_priority
from . import filter_cards_by_due_date
from . import filter_cards_by_parent
from . import filter_cards_move_up_one_parent
from . import get_selected_cards_and_their_indexes
from . import implement_lower_level_detail
from . import increment_card_importance
from . import insert_as_policy_action_new_card_from_templates
from . import jump_to_implementation_card
from . import jump_to_policy_action
from . import load_gui
from . import load_state_from_file
from . import load_template_card
from . import mark_action_completed
from . import move_actions_down
from . import move_actions_up
from . import move_my_cards_down
from . import move_my_cards_up
from . import move_their_cards_down
from . import move_their_cards_up
from . import open_display_list_of_actions
from . import paste_action_as_duplicate
from . import paste_action_notes
from . import paste_action_resources
from . import paste_actions_as_alias
from . import present_card_list
from . import remove_selected_action_resources
from . import reset_card_starting_date
from . import save_as_template_card
from . import select_actions
from . import set_action_client
from . import set_action_complete_time
from . import set_action_description
from . import set_action_name
from . import set_action_owner
from . import set_action_time_expected
from . import set_card_name
from . import set_color_to_actions
from . import set_color_to_cards
from . import set_dead_line
from . import set_start_from
from . import shift_actions_dead_lines_by
from . import shift_actions_dead_lines_hours_by
from . import shift_cards_dead_lines
from . import shift_resources
from . import show_action_information
from . import show_datetime_setter_dead_line
from . import show_datetime_setter_start_from
from . import show_email_creator1
from . import show_minutes_setter
from . import show_my_card_information
from . import show_their_card_information
from . import sync_notification_handler
from .abc import InteractorABC


class Interactor(InteractorABC):

    def __init__(self, entities: EntitiesABC, presenters: PresentersABC, gateway: GatewayABC):
        self._entities = entities
        self._presenters = presenters
        self._gateway = gateway
        self._keymaps = KeyMaps()
        self._recursive_counter = 0

        entities.attach_to_synchronizer(self.synchronizer_notification_handler)

    # GUI
    def load_gui(self, gui_name: str):
        load_gui.execute(self._entities, self._presenters, self._gateway, gui_name)

    # Save
    def save_state(self):
        self.save_to_file(self._gateway.auto_save_path)

    def save_state_silently(self):
        self.save_state_to_file_silently(self._gateway.auto_save_path)

    def save_state_to_file_silently(self, file_name):
        self._gateway.save_file(file_name, self._entities.state)

    def save_to_file(self, file_name: str):
        self.save_state_to_file_silently(file_name)
        self.feed_back_user_by_popup('File saved!', f'Files was successfully saved to \n{file_name}', 600, 100)

    def load_state_from_file(self, file_name: str):
        load_state_from_file.execute(self._entities, self._gateway, self._presenters, file_name)

    def save_as_template_card(self, file_name: str):
        save_as_template_card.execute(self._entities, self._gateway, file_name)

    def load_template_card(self, file_name: str):
        load_template_card.execute(self._entities, self._gateway, self._presenters, file_name)

    # Cards
    def add_new_card(self):
        add_new_card_from_templates.execute(self._entities, self._gateway, self._presenters)

    def insert_new_card(self):
        insert_as_policy_action_new_card_from_templates.execute(self._entities, self._gateway, self._presenters)

    def duplicate_selected_card(self):
        duplicate_selected_card.execute(self._entities, self._presenters, self._entities.active_card)

    def delete_selected_my_cards(self, indexes: Tuple[int]):
        delete_selected_my_cards.execute(self._entities, self._presenters, indexes)

    def delete_selected_their_cards(self, indexes: Tuple[int]):
        delete_selected_their_cards.execute(self._entities, self._presenters, indexes)

    def set_card_name(self, card_name: str):
        set_card_name.execute(self._entities, self._presenters, card_name)

    def increment_importance(self, increment: int):
        increment_card_importance.execute(self._entities, self._presenters, increment)

    def shift_cards_dead_lines_by(self, days: int, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...]):
        shift_cards_dead_lines.execute(self._entities, self._presenters, days, indexes1, indexes2)

    def show_my_card_information(self, indexes: Tuple[int]):
        show_my_card_information.execute(self._entities, self._presenters, indexes)

    def show_their_card_information(self, indexes: Tuple[int]):
        show_their_card_information.execute(self._entities, self._presenters, indexes)

    def move_my_cards_up(self, indexes: Tuple[int, ...]):
        move_my_cards_up.execute(self._entities, self._presenters, indexes)

    def move_my_cards_down(self, indexes: Tuple[int, ...]):
        move_my_cards_down.execute(self._entities, self._presenters, indexes)

    def move_their_cards_up(self, indexes: Tuple[int, ...]):
        move_their_cards_up.execute(self._entities, self._presenters, indexes)

    def move_their_cards_down(self, indexes: Tuple[int, ...]):
        move_their_cards_down.execute(self._entities, self._presenters, indexes)

    def set_color_to_cards(self, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...], color):
        set_color_to_cards.execute(self._entities, self._presenters, color, indexes1, indexes2)

    def set_color_to_actions(self, indexes: Tuple[int, ...], color):
        set_color_to_actions.execute(self._entities, self._presenters, color, indexes)

    # Filter
    def hide_finished_cards(self):
        self._entities.hide_finished_cards()
        present_card_list.execute(self._entities, self._presenters)

    def unhide_finished_cards(self):
        self._entities.unhide_finished_cards()
        present_card_list.execute(self._entities, self._presenters)

    def toggle_hide_finished_cards(self):
        self._entities.toggle_hide_finished_cards()
        self.filter_cards_with_keyword(self._entities.filter_key, self._entities.filter_mode)
        present_card_list.execute(self._entities, self._presenters)

    def filter_cards_by_due_date(self):
        filter_cards_by_due_date.execute(self._entities, self._presenters)

    def filter_cards_by_parent(self):
        filter_cards_by_parent.execute(self._entities, self._presenters)

    def filter_by_priority(self, priority: int):
        filter_by_priority.execute(self._entities, self._presenters, priority)

    def clear_filter_by_priority(self):
        clear_filter_by_priority.execute(self._entities, self._presenters)

    def clear_all_filters(self):
        self._entities.clear_all_filters()
        present_card_list.execute(self._entities, self._presenters)

    def clear_filter_due_date(self):
        self._entities.clear_filter_due_date()
        present_card_list.execute(self._entities, self._presenters)

    def clear_filter_by_parent(self):
        self._entities.clear_filter_by_parent()
        present_card_list.execute(self._entities, self._presenters)

    def filter_move_up_one_parent(self):
        filter_cards_move_up_one_parent.execute(self._entities, self._presenters)
        present_card_list.execute(self._entities, self._presenters)

    def convert_selected_cards_to_actions(self, left_indexes_and_right_indexes: Tuple[Tuple[int, ...], ...]):
        args = self._entities, self._presenters, left_indexes_and_right_indexes, self.feed_back_user_by_popup
        convert_cards_to_actions.execute(*args)

        all_cards, indexes = get_selected_cards_and_their_indexes.execute(self._entities,
                                                                          left_indexes_and_right_indexes)
        cards_selected = tuple(card for (n, card) in enumerate(all_cards) if n in indexes)
        for card in cards_selected:
            self._entities.remove_card(card)

    def reset_card_starting_date(self, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...]):
        args = indexes1, indexes2, self.show_my_card_information, self.show_their_card_information, self._entities, self._presenters
        reset_card_starting_date.execute(*args)

    def open_filter_setting(self):
        e = self._entities
        p = self._presenters
        f = e.filter

        def filter_by_due_date(date: datetime.datetime):
            e.set_filter_due_date(date)
            present_card_list.execute(e, p)

        def filter_by_parent():
            e.set_active_card(initially_active_card)
            self.filter_cards_by_parent()

        def reset_active_card():
            e.set_active_card(initially_active_card)
            present_card_list.execute(e, p)

        initially_active_card = e.active_card
        commands = {
            'filter_with_keyword': self._filter_cards_with_keyword,
            'clear_search': self.clear_card_filter,
            'hide_finished': self.hide_finished_cards,
            'show_finished': self.unhide_finished_cards,
            'filter_by_due_date': filter_by_due_date,
            'clear_filter_by_due_date': self.clear_filter_due_date,
            'filter_by_parent': filter_by_parent,
            'clear_filter_by_parent': self.clear_filter_by_parent,
            'filter_by_priority': self.filter_by_priority,
            'clear_filter_by_priority': self.clear_filter_by_priority,
            'clear_all_filters': self.clear_all_filters,
            'reset_active_card': reset_active_card,
        }

        states = {
            'search_modes': e.filter.all_filter_modes,
            'show_finished': not f.hide_finished_cards,
            'due_date': f.filter_due_date_time or Utilities.datetime_to_str(datetime.datetime.today()),
            'filter_by_date': f.filtering_by_due_date,
            'filter_by_parent': f.filtering_by_parent,
            'filter_by_priority': f.filtering_by_priority,
            'priority_max': Priority().priority_max,
            'priority_min': Priority().priority_min,
        }
        p.open_filter_setting(commands, states)

    @property
    def active_card(self):
        return self._entities.active_card

    @property
    def active_card_in_my_ball(self) -> bool:
        return self._entities.active_card_is_in_my_cards

    @property
    def active_card_index(self) -> int:
        return self._entities.active_card_index

    # Action
    def add_new_action(self):
        add_new_action.execute(self._entities, self._presenters)

    def delete_selected_actions(self, indexes: Tuple[int]):
        delete_selected_actions.execute(self._entities, self._presenters, indexes)

    def set_action_name(self, action_name: str, actions_indexes: Tuple[int, ...]):
        set_action_name.execute(self._entities, self._presenters, action_name, actions_indexes)

    def set_action_owner(self, owner_name: str, actions_indexes: Tuple[int, ...]):
        set_action_owner.execute(self._entities, self._presenters, owner_name, actions_indexes)

    def mark_action_completed(self, done_or_not: bool, actions_indexes: Tuple[int, ...] = None):
        mark_action_completed.execute(self._entities, self._presenters, done_or_not, actions_indexes)

    def set_action_description(self, description: str, actions_indexes: Tuple[int, ...]):
        set_action_description.execute(self._entities, self._presenters, description[:-1], actions_indexes)

    def set_action_time_expected(self, time_expected: str, actions_indexes: Tuple[int, ...]):
        set_action_time_expected.execute(self._entities, self._presenters, time_expected, actions_indexes)

    def show_action_information(self, indexes: Tuple[int]):
        select_actions.execute(self._entities, indexes)
        show_action_information.execute(self._entities, self._presenters, indexes)

    def move_actions_up(self, indexes: Tuple[int, ...]):
        move_actions_up.execute(self._entities, self._presenters, indexes)

    def move_actions_down(self, indexes: Tuple[int, ...]):
        move_actions_down.execute(self._entities, self._presenters, indexes)

    def set_dead_line(self, dead_line_str: str, indexes: Tuple[int, ...]):
        def ask_user(message: str, **kwargs):
            self.feed_back_user_by_popup('Changing multiple actions!', message, 400, 400, **kwargs)

        set_dead_line.execute(self._entities, self._presenters, dead_line_str, indexes, ask_user)

    def set_start_from(self, start_from_str: str, indexes: Tuple[int, ...]):
        def ask_user(message: str, **kwargs):
            self.feed_back_user_by_popup('Changing multiple actions!', message, 400, 400, **kwargs)

        set_start_from.execute(self._entities, self._presenters, start_from_str, indexes, ask_user)

    def shift_actions_dead_lines_by(self, days: int, indexes: Tuple[int, ...]):
        shift_actions_dead_lines_by.execute(self._entities, self._presenters, days, indexes)

    def shift_actions_dead_lines_hours_by(self, hours: int, indexes: Tuple[int, ...]):
        shift_actions_dead_lines_hours_by.execute(self._entities, self._presenters, hours, indexes)

    def set_client(self, client_name: str, actions_indexes: Tuple[int, ...]):
        set_action_client.execute(self._entities, self._presenters, client_name, actions_indexes)

    def copy_actions(self):
        selected_actions = self._entities.selected_actions
        self._entities.copy_actions(selected_actions)

    def cut_actions(self):
        self._entities.turn_on_cut_mode()
        self.copy_actions()

    @property
    def copied_actions(self) -> tuple:
        return self._entities.copied_actions

    def paste_actions_as_duplicate(self):
        paste_action_as_duplicate.execute(self._entities, self._presenters)

    def paste_resources(self):
        paste_action_resources.execute(self._entities, self._presenters)

    def paste_description(self):
        paste_action_notes.execute(self._entities, self._presenters)

    def paste_actions_as_alias(self):
        paste_actions_as_alias.execute(self._entities, self._presenters, self.feed_back_user_by_popup)

    def implement_lower_level_detail(self, *_):
        implement_lower_level_detail.execute(self._entities, self._presenters)

    def abstract_out_card_as_an_action_and_copy(self, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...]):
        abstract_out.execute(self._entities, indexes1, indexes2, self.feed_back_user_by_popup)

    def jump_to_implementation_card(self, callback):
        jump_to_implementation_card.execute(self._entities, self._presenters, callback)

    def jump_to_policy_action(self, callback):
        jump_to_policy_action.execute(self._entities, self._presenters, callback)

    def jump_to_card_list(self, callback: Callable):
        callback(self._entities.active_card_is_in_my_cards, self._entities.active_card_index)

    def jump_to_action_list(self, callback: Callable):
        callback(self._entities.active_action_index)

    # Action Resources
    def select_action_resources(self, indexes: tuple):
        self._entities.select_action_resources(indexes)

    def add_action_resources(self, paths: tuple):
        add_action_resources.execute(self._entities, self._presenters, paths)

    def remove_selected_action_resources(self, callback: Callable = None):
        remove_selected_action_resources.execute(self._entities, self._presenters, callback)

    def shift_resources(self, shift: int, callback=None):
        shift_resources.execute(self._entities, self._presenters, shift, callback)

    def open_resources(self):
        for uri in self._entities.get_selected_uris():
            Utilities.open_file(uri)

    def open_folder_of_resources(self):
        folder_to_open = set()
        for uri in self._entities.get_selected_uris():
            split_by_slash = uri.split(os_identifier.DIRECTORY_SEPARATOR)
            last_element = split_by_slash[-1]
            if '.' not in last_element:
                folder_to_open.add(uri)
            else:
                folder_to_open.add(uri.replace(last_element, ''))

        for folder in folder_to_open:
            Utilities.open_file(folder)

    # Synchronize
    def synchronizer_notification_handler(self, **kwargs):
        sync_notification_handler.execute(self._entities, self._presenters, **kwargs)

    # Sorter
    def sort_cards(self):
        self._sort_cards(self._entities.sort_cards_by_the_same_method)

    def sort_cards_by_deadline(self):
        self._sort_cards(self._entities.sort_cards_by_deadline)

    def sort_cards_by_name(self):
        self._sort_cards(self._entities.sort_cards_by_name)

    def sort_cards_by_current_owner(self):
        self._sort_cards(self._entities.sort_cards_by_current_owner)

    def sort_cards_by_current_client(self):
        self._sort_cards(self._entities.sort_cards_by_current_client)

    def sort_cards_by_color(self):
        self._sort_cards(self._entities.sort_cards_by_color)

    def sort_by_importance(self):
        self._sort_cards(self._entities.sort_cards_by_importance)

    def _sort_cards(self, sort_method):
        self._entities.clear_temporarily_display_card()
        sort_method()
        present_card_list.execute(self._entities, self._presenters)

    # Keyboard shortcut
    def set_active_keymap(self, name: str):
        self._keymaps.set_active_keymap(name)

    def clear_keyboard_shortcuts(self):
        self._keymaps.active_keymap.clear()

    def add_new_keyboard_shortcut(self, key_combo: tuple, command_and_feedback: tuple):
        self._keymaps.active_keymap.add_new_keyboard_shortcut(key_combo, command_and_feedback)

    @property
    def keymaps(self) -> KeyMaps:
        return self._keymaps

    # Setup Teardown
    def set_up(self):
        loaded = True

        if not os.path.exists(self._gateway.home_folder):
            os.mkdir(self._gateway.home_folder)
        if not os.path.exists(self._gateway.state_folder):
            os.mkdir(self._gateway.state_folder)
        if not os.path.exists(self._gateway.graph_folder_path):
            os.mkdir(self._gateway.graph_folder_path)
        if not os.path.exists(self._gateway.gantt_chart_folder_path):
            os.mkdir(self._gateway.gantt_chart_folder_path)
        if not os.path.exists(self._gateway.keyboard_config_folder_path):
            os.mkdir(self._gateway.keyboard_config_folder_path)
        try:
            self.load_state_from_file(self._gateway.auto_save_path)
        except:
            loaded = False
        if loaded:
            self.show_my_card_information((0,))
            self.show_their_card_information((0,))
            self.show_action_information((0,))

    def close(self, command):
        self.save_to_file(self._gateway.auto_save_path)
        command()

    # Mail
    def create_mail_menu(self, ask_folder: Callable, configure_menu: Callable):
        create_mail_menu.execute(self._entities, self._gateway, self._presenters, ask_folder, configure_menu)

    @property
    def state_folder(self) -> str:
        return self._gateway.state_folder

    @property
    def home_folder(self) -> str:
        return self._gateway.home_folder

    @property
    def save_state_path(self) -> str:
        return self._gateway.auto_save_path

    @property
    def graph_folder_path(self) -> str:
        return self._gateway.graph_folder_path

    @property
    def mail_template_path(self) -> str:
        return self._gateway.mail_template_path

    @property
    def cards_template_path(self) -> str:
        return self._gateway.cards_template_path

    @property
    def keyboard_config_folder_path(self) -> str:
        return self._gateway.keyboard_config_folder_path

    def make_email(self):
        show_email_creator1.execute(self._entities, self._presenters, self._gateway)

    # Search box
    def filter_cards_with_keyword(self, keyword: str, search_mode: str):
        if keyword.strip() != '':
            self._filter_cards_with_keyword(keyword, search_mode)

    def clear_card_filter(self):
        initially_selected_card = self._entities.active_card
        self._entities.clear_filter_key()
        self._entities.clear_filter_mode()
        self._entities.set_filter_key('', self.search_mode[0])
        self._entities.set_active_card(initially_selected_card)
        present_card_list.execute(self._entities, self._presenters)

    def _filter_cards_with_keyword(self, keyword: str, search_mode: str):
        self._entities.set_filter_key(keyword, search_mode)
        present_card_list.execute(self._entities, self._presenters)
        self._entities.clear_show_this_card()

    @property
    def search_mode(self) -> Tuple[str, ...]:
        return self._entities.all_filter_modes

    # Popup
    def feed_back_user_by_popup(self, title: str, text: str, width=200, height=200, **kwargs):
        self._presenters.feed_back_user_by_popup(title, text, width, height, **kwargs)

    def show_minutes_setter(self, indexes):
        show_minutes_setter.execute(self._entities, self._presenters, self._gateway, indexes)

    def show_datetime_setter_start_from(self, indexes):
        show_datetime_setter_start_from.execute(self._entities, self._presenters, self._gateway, indexes)

    def show_datetime_setter_dead_line(self, indexes):
        show_datetime_setter_dead_line.execute(self._entities, self._presenters, self._gateway, indexes)

    # Export
    def export_actions_list(self, file_name: str):
        export_actions_list.execute(file_name, self._entities, self._gateway)

    def export_gantt_chart_data(self, max_level: int = None):
        export_gantt_chart_data.execute(self._entities, self._gateway, max_level=max_level)

    def open_display_progress_dialogue(self):
        options = {'title': 'Tasks completed during...'}
        self._presenters.open_display_progress_dialogue(self.display_progress, **options)

    def open_display_new_tasks_dialogue(self):
        options = {'title': 'New tasks added between...'}
        self._presenters.open_display_progress_dialogue(self.display_new_tasks, **options)

    def open_display_due_tasks_dialogue(self):
        options = {'title': 'Tasks due during...', 'from': '2022/1/1'}
        self._presenters.open_display_progress_dialogue(self.display_due_tasks, **options)

    def open_display_due_tasks_dialogue_my_ball(self):
        options = {'title': 'Tasks due during...', 'from': '2022/1/1'}
        self._presenters.open_display_progress_dialogue(self.display_due_tasks_my_ball, **options)

    def open_display_due_tasks_dialogue_their_ball(self):
        options = {'title': 'Tasks due during...', 'from': '2022/1/1'}
        self._presenters.open_display_progress_dialogue(self.display_due_tasks_their_ball, **options)

    def open_display_list_of_actions(self):
        open_display_list_of_actions.execute(self._entities, self._presenters, self.sort_cards)

    def display_progress(self, from_: str, to_: str):
        display_progress.execute(from_, to_, self.feed_back_user_by_popup, self._entities)

    def display_new_tasks(self, from_: str, to_: str):
        display_new_tasks.execute(from_, to_, self.feed_back_user_by_popup, self._entities)

    def display_due_tasks(self, from_: str, to_: str):
        display_due_tasks.execute(from_, to_, self.feed_back_user_by_popup, self._entities)

    def display_due_tasks_my_ball(self, from_: str, to_: str):
        display_due_tasks_my_ball.execute(from_, to_, self.feed_back_user_by_popup, self._entities)

    def display_due_tasks_their_ball(self, from_: str, to_: str):
        display_due_tasks_their_ball.execute(from_, to_, self.feed_back_user_by_popup, self._entities)

    def display_selected_card_as_a_graph_on_the_browser(self):
        save, feedback = self.save_state_silently, self.feed_back_user_by_popup
        draw_graph_on_browser.execute(self._entities, self._gateway, save, feedback)

    def display_selected_card_as_a_graph_on_the_browser_with_dynamic_config(self):
        save, feedback = self.save_state_silently, self.feed_back_user_by_popup
        kwargs = {'configure_dynamically': True}
        draw_graph_on_browser.execute(self._entities, self._gateway, save, feedback, **kwargs)

    def increment_recursive_counter(self):
        self._recursive_counter += 1

    def reset_recursive_counter(self):
        self._recursive_counter = 0

    @property
    def recursive_counter(self):
        return self._recursive_counter
