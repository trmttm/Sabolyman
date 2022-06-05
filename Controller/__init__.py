from interface_view import ViewABC

import WidgetNames
from Interactor import InteractorABC
from . import state as s


def configure_controller(v: ViewABC, i: InteractorABC):
    f = v.bind_command_to_widget
    wn = WidgetNames

    f(wn.button_add_new_my_card, lambda: i.add_new_card())
    f(wn.button_delete_selected_my_card, lambda: i.delete_selected_cards(s.get_my_cards_selected_indexes(v)))

    # My Cards
    f(wn.tree_my_cards, lambda: i.show_card_information(s.get_my_cards_selected_indexes(v)))
    f(wn.entry_card_name, lambda *_: i.set_card_name(s.get_card_name(v)))
    f(wn.entry_dead_line, lambda *_: i.set_dead_line(s.get_dead_line_str(v)))
    f(wn.button_add_new_action, lambda: i.add_new_action())

    # Action
    f(wn.tree_card_actions, lambda: i.show_action_information(s.get_actions_selected_indexes(v)))
    f(wn.entry_action_name, lambda *_: i.set_action_name(s.get_action_name(v)))
    f(wn.entry_action_owner, lambda *_: i.set_action_owner(s.get_action_owner_name(v)))
    f(wn.check_button_action_done, lambda *_: i.set_action_is_done_or_not(s.get_action_is_done_or_not(v)))
