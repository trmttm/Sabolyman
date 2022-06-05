from interface_view import ViewABC

import WidgetNames
from Interactor import InteractorABC
from . import state as s


def configure_controller(v: ViewABC, i: InteractorABC):
    f = v.bind_command_to_widget
    wn = WidgetNames

    # My Cards
    f(wn.button_add_new_my_card, lambda: i.add_new_card())
    f(wn.button_delete_selected_my_card, lambda: i.delete_selected_cards(s.get_my_cards_selected_indexes(v)))
    f(wn.tree_my_cards, lambda: i.show_card_information(s.get_my_cards_selected_indexes(v)))
    f(wn.entry_card_name, lambda *_: i.set_card_name(s.get_card_name(v)))
    f(wn.entry_dead_line, lambda *_: i.set_dead_line(s.get_dead_line_str(v)))

    # Action
    f(wn.button_add_new_action, lambda: i.add_new_action())
    f(wn.button_delete_selected_actions, lambda: i.delete_selected_actions(s.get_actions_selected_indexes(v)))
    f(wn.tree_card_actions, lambda: i.show_action_information(s.get_actions_selected_indexes(v)))
    f(wn.entry_action_name, lambda *_: i.set_action_name(s.get_action_name(v)))
    f(wn.entry_action_owner, lambda *_: i.set_action_owner(s.get_action_owner_name(v)))
    f(wn.check_button_action_done, lambda *_: i.set_action_is_done_or_not(s.get_action_is_done_or_not(v)))
    f(wn.text_box_action_description, lambda *_: i.set_action_description(s.get_action_description(v)))
    f(wn.entry_action_time_expected, lambda *_: i.set_action_time_expected(s.get_action_time_expected(v)))


def configure_menu_bar(v: ViewABC, i: InteractorABC):
    menu_bar_model = {
        'File': {
            'Save': lambda: i.save_to_file(v.select_save_file()),
            'Load': lambda: i.load_state_from_file(v.select_open_file()),
        },
    }
    v.update_menu_bar(menu_bar_model)
