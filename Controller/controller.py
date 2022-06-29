from interface_view import ViewABC

import WidgetNames
from Interactor import InteractorABC
from . import state as s


def configure_controller(v: ViewABC, i: InteractorABC):
    f = v.bind_command_to_widget
    wn = WidgetNames
    ai = s.get_actions_selected_indexes

    # My Cards
    f(wn.button_add_new_my_card, lambda: i.add_new_card())
    f(wn.button_move_up_selected_my_card, lambda: i.move_my_cards_up(s.get_my_cards_selected_indexes(v)))
    f(wn.button_move_down_selected_my_card, lambda: i.move_my_cards_down(s.get_my_cards_selected_indexes(v)))
    f(wn.button_delete_selected_my_card, lambda: i.delete_selected_my_cards(s.get_my_cards_selected_indexes(v)))

    f(wn.button_move_up_selected_their_card, lambda: i.move_their_cards_up(s.get_their_cards_selected_indexes(v)))
    f(wn.button_move_down_selected_their_card, lambda: i.move_their_cards_down(s.get_their_cards_selected_indexes(v)))
    f(wn.button_delete_selected_their_card,
      lambda: i.delete_selected_their_cards(s.get_their_cards_selected_indexes(v)))

    f(wn.tree_my_cards, lambda: i.show_my_card_information(s.get_my_cards_selected_indexes(v)))
    f(wn.tree_their_cards, lambda: i.show_their_card_information(s.get_their_cards_selected_indexes(v)))
    f(wn.entry_card_name, lambda *_: i.set_card_name(s.get_card_name(v)))
    f(wn.entry_dead_line, lambda *_: i.set_dead_line(s.get_dead_line_str(v)))
    f(wn.entry_card_client, lambda *_: i.set_client(s.get_client(v)))

    # Action
    f(wn.button_add_new_action, lambda: i.add_new_action())
    f(wn.button_delete_selected_actions, lambda: i.delete_selected_actions(ai(v)))
    f(wn.button_move_up_selected_actions, lambda: i.move_actions_up(ai(v)))
    f(wn.button_move_down_selected_actions, lambda: i.move_actions_down(ai(v)))
    f(wn.tree_card_actions, lambda: i.show_action_information(ai(v)))
    f(wn.entry_action_name, lambda *_: i.set_action_name(s.get_action_name(v), ai(v)))
    f(wn.entry_action_owner, lambda *_: i.set_action_owner(s.get_action_owner_name(v), ai(v)))
    f(wn.check_button_action_done, lambda *_: i.mark_action_completed(s.get_action_is_done_or_not(v), ai(v)))
    f(wn.text_box_action_description, lambda *_: i.set_action_description(s.get_action_description(v)))
    f(wn.entry_action_time_expected, lambda *_: i.set_action_time_expected(s.get_action_time_expected(v), ai(v)))
