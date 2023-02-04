from typing import Callable

from interface_view import ViewABC

import WidgetNames
from Interactor import InteractorABC
from . import state as s

recursive_counter = 0


def configure_controller(v: ViewABC, i: InteractorABC):
    f = v.bind_command_to_widget
    wn = WidgetNames
    ai = s.get_actions_selected_indexes

    def prevent_unintended_action_property_change_when_tab_is_pressed(method: Callable):
        global recursive_counter
        if recursive_counter == 0:
            recursive_counter += 1
            method()
            action_selected_indexes = s.get_actions_selected_indexes(v)
            if len(action_selected_indexes) > 0:
                v.focus(WidgetNames.tree_card_actions, tree_item_position=action_selected_indexes)
        else:
            recursive_counter = 0

    wrapper = prevent_unintended_action_property_change_when_tab_is_pressed

    # prevent unintended action property change when tab is pressed
    v.bind_tree_enter(lambda: upon_action_tree_entrance(v))

    # Search box
    v.set_combobox_values(wn.combobox_search_mode, i.search_mode)
    v.set_value(wn.combobox_search_mode, i.search_mode[0])
    f(wn.entry_search_box, lambda *_: i.filter_cards_with_keyword(s.get_search_box_entry(v), s.get_search_model(v)))
    f(wn.combobox_search_mode,
      lambda *_: i.filter_cards_with_keyword(s.get_search_box_entry(v), s.get_search_model(v)))
    f(wn.btn_clear_search, lambda *_: i.clear_card_filter())

    # My Cards
    f(wn.button_add_new_my_card, lambda: i.add_new_card())
    f(wn.button_move_up_selected_my_card, lambda: i.move_my_cards_up(s.get_left_tree_selected_indexes(v)))
    f(wn.button_move_down_selected_my_card, lambda: i.move_my_cards_down(s.get_left_tree_selected_indexes(v)))
    f(wn.button_delete_selected_my_card, lambda: i.delete_selected_my_cards(s.get_left_tree_selected_indexes(v)))

    f(wn.button_move_up_selected_their_card, lambda: i.move_their_cards_up(s.get_right_tree_selected_indexes(v)))
    f(wn.button_move_down_selected_their_card,
      lambda: i.move_their_cards_down(s.get_right_tree_selected_indexes(v)))
    f(wn.button_delete_selected_their_card,
      lambda: i.delete_selected_their_cards(s.get_right_tree_selected_indexes(v)))

    f(wn.tree_my_cards, lambda: i.show_my_card_information(s.get_left_tree_selected_indexes(v)))
    f(wn.tree_their_cards, lambda: i.show_their_card_information(s.get_right_tree_selected_indexes(v)))
    f(wn.entry_card_name, lambda *_: i.set_card_name(s.get_card_name(v)))

    # Action
    f(wn.button_add_new_action, lambda: i.add_new_action())
    f(wn.button_delete_selected_actions, lambda: i.delete_selected_actions(ai(v)))
    f(wn.button_move_up_selected_actions, lambda: i.move_actions_up(ai(v)))
    f(wn.button_move_down_selected_actions, lambda: i.move_actions_down(ai(v)))
    f(wn.button_set_duration, lambda: i.show_minutes_setter())
    f(wn.tree_card_actions, lambda: i.show_action_information(ai(v)))
    f(wn.entry_action_name, lambda *_: wrapper(lambda *_: i.set_action_name(s.get_action_name(v), ai(v))))
    f(wn.entry_action_owner, lambda *_: wrapper(lambda *_: i.set_action_owner(s.get_action_owner_name(v), ai(v))))
    f(wn.entry_action_client, lambda *_: wrapper(lambda *_: i.set_client(s.get_client(v), ai(v))))
    f(wn.entry_action_time_expected,
      lambda *_: wrapper(lambda *_: i.set_action_time_expected(s.get_action_time_expected(v), ai(v))))
    f(wn.entry_action_dead_line, lambda *_: wrapper(lambda *_: i.set_dead_line(s.get_dead_line_str(v), ai(v))))
    f(wn.check_button_action_done, lambda *_: i.mark_action_completed(s.get_action_is_done_or_not(v), ai(v)))
    f(wn.text_box_action_description, lambda *_: i.set_action_description(s.get_action_description(v), ai(v))),


def upon_action_tree_entrance(v: ViewABC):
    global recursive_counter
    v.focus('root'), WidgetNames.tree_card_actions
    recursive_counter = 0
