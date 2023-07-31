from typing import Callable

import WidgetNames
import clipboard
import os_identifier
from Interactor import InteractorABC
from interface_view import ViewABC

from . import state as s
from . import utilities


def configure_controller(v: ViewABC, i: InteractorABC):
    f = v.bind_command_to_widget
    wn = WidgetNames
    ai = s.get_actions_selected_indexes

    def prevent_unintended_action_property_change_when_tab_is_pressed(method: Callable, i: InteractorABC):
        if i.recursive_counter == 0:
            i.increment_recursive_counter()
            method()
            action_selected_indexes = s.get_actions_selected_indexes(v)
            if len(action_selected_indexes) > 0:
                v.focus(WidgetNames.tree_card_actions, tree_item_position=action_selected_indexes)
        else:
            i.reset_recursive_counter()

    wrapper = prevent_unintended_action_property_change_when_tab_is_pressed

    # prevent unintended action property change when tab is pressed
    v.bind_tree_enter(lambda: upon_action_tree_entrance(v, i), wn.tree_card_actions)
    v.bind_widget_entry(wn.entry_action_name, lambda: i.reset_recursive_counter())
    v.bind_widget_entry(wn.entry_action_dead_line, lambda: i.reset_recursive_counter())
    v.bind_widget_entry(wn.entry_action_client, lambda: i.reset_recursive_counter())
    v.bind_widget_entry(wn.entry_action_owner, lambda: i.reset_recursive_counter())
    v.bind_widget_entry(wn.entry_action_start_from, lambda: i.reset_recursive_counter())
    v.bind_widget_entry(wn.entry_action_time_expected, lambda: i.reset_recursive_counter())

    # My Cards
    f(wn.button_add_new_my_card, lambda: i.add_new_card())
    f(wn.button_insert_new_my_card, lambda: i.insert_new_card())
    f(wn.button_move_up_selected_my_card, lambda: i.move_my_cards_up(s.get_left_tree_selected_indexes(v)))
    f(wn.button_move_down_selected_my_card, lambda: i.move_my_cards_down(s.get_left_tree_selected_indexes(v)))
    f(wn.button_delete_selected_my_card, lambda: i.delete_selected_my_cards(s.get_left_tree_selected_indexes(v)))

    f(wn.button_move_up_selected_their_card, lambda: i.move_their_cards_up(s.get_right_tree_selected_indexes(v)))
    f(wn.button_move_down_selected_their_card,
      lambda: i.move_their_cards_down(s.get_right_tree_selected_indexes(v)))
    f(wn.button_delete_selected_their_card,
      lambda: i.delete_selected_their_cards(s.get_right_tree_selected_indexes(v)))
    f(wn.button_importance_down, lambda: i.increment_importance(-1))
    f(wn.button_importance_up, lambda: i.increment_importance(1))

    f(wn.tree_my_cards, lambda: i.show_my_card_information(s.get_left_tree_selected_indexes(v)))
    f(wn.tree_their_cards, lambda: i.show_their_card_information(s.get_right_tree_selected_indexes(v)))
    f(wn.entry_card_name, lambda *_: i.set_card_name(s.get_card_name(v)))

    # Action
    f(wn.button_display_resources, lambda: i.display_resources_of_selected_action())
    f(wn.button_add_new_action, lambda: i.add_new_action())
    f(wn.button_delete_selected_actions, lambda: i.delete_selected_actions(ai(v)))
    f(wn.button_move_up_selected_actions, lambda: i.move_actions_up(ai(v)))
    f(wn.button_move_down_selected_actions, lambda: i.move_actions_down(ai(v)))
    f(wn.button_set_duration, lambda: i.show_minutes_setter(ai(v)))
    f(wn.button_set_start_from, lambda: i.show_datetime_setter_start_from(ai(v)))
    f(wn.button_set_deadline, lambda: i.show_datetime_setter_dead_line(ai(v)))
    f(wn.tree_card_actions, lambda: i.show_action_information(ai(v)))
    f(wn.entry_action_name, lambda *_: wrapper(lambda *_: i.set_action_name(s.get_action_name(v), ai(v)), i))
    f(wn.entry_action_owner, lambda *_: wrapper(lambda *_: i.set_action_owner(s.get_action_owner_name(v), ai(v)), i))
    f(wn.entry_action_client, lambda *_: wrapper(lambda *_: i.set_client(s.get_client(v), ai(v)), i))
    f(wn.entry_action_time_expected,
      lambda *_: wrapper(lambda *_: i.set_action_time_expected(s.get_action_time_expected(v), ai(v)), i))
    f(wn.entry_action_dead_line, lambda *_: wrapper(lambda *_: i.set_dead_line(s.get_dead_line_str(v), ai(v)), i))
    f(wn.entry_action_start_from, lambda *_: wrapper(lambda *_: i.set_start_from(s.get_start_from_str(v), ai(v)), i))
    f(wn.check_button_action_done, lambda *_: i.mark_action_completed(s.get_action_is_done_or_not(v), ai(v)))
    f(wn.check_button_action_scheduled, lambda *_: i.mark_action_scheduled(s.get_action_scheduled_or_not(v), ai(v)))
    f(wn.text_box_action_description, lambda *_: i.set_action_description(s.get_action_description(v), ai(v)))

    # DND
    def callback(e):
        i.add_action_resources(utilities.get_paths(e))

    # Action Resources
    v.bind_tree_enter(lambda: upon_resources_tree_entrance(i), wn.tree_action_resources)

    def select_resources_tree(indexes: tuple):
        v.select_multiple_tree_items(wn.tree_action_resources, indexes)

    v.bind_upon_drag_and_drop_drop(wn.tree_action_resources, callback)
    f(wn.tree_action_resources, lambda: i.select_action_resources(s.get_action_resources_selected_indexes(v)))
    f(wn.button_add_new_resources, lambda: i.add_action_resources((v.select_open_file(),)))
    f(wn.button_delete_selected_resources, lambda: i.remove_selected_action_resources(select_resources_tree))
    f(wn.button_move_up_selected_resources, lambda: i.shift_resources(-1, select_resources_tree))
    f(wn.button_move_down_selected_resources, lambda: i.shift_resources(1, select_resources_tree))
    f(wn.button_open_resources, lambda: i.open_resources())
    f(wn.button_open_resource_folders, lambda: i.open_folder_of_resources())


def upon_action_tree_entrance(v: ViewABC, i: InteractorABC):
    v.focus('root'), WidgetNames.tree_card_actions
    i.reset_recursive_counter()


def upon_resources_tree_entrance(i: InteractorABC):
    key = "SBLM Resources"
    clipboard_text = clipboard.paste()
    if clipboard_text[:len(key)] == key:
        # clipboard_text = clipboard_text.replace(key + os_identifier.NEW_LINE_SYMBOL, '')
        # clipboard_text = clipboard_text.replace(os_identifier.NEW_LINE_SYMBOL, ',')
        clipboard_text = clipboard_text.replace(key, '')
        clipboard_text = clipboard_text.replace(os_identifier.NEW_LINE_SYMBOL, ',')
        paths = tuple(p for p in clipboard_text.split(',') if p.strip() != '')
        i.add_action_resources(paths)
        clipboard.copy('')
