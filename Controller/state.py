from typing import Tuple

from interface_view import ViewABC

import WidgetNames


def get_my_cards_selected_indexes(v: ViewABC) -> Tuple[int]:
    return v.get_selected_tree_item_indexes(WidgetNames.tree_my_cards)


def get_their_cards_selected_indexes(v: ViewABC) -> Tuple[int]:
    return v.get_selected_tree_item_indexes(WidgetNames.tree_their_cards)


def get_actions_selected_indexes(v: ViewABC) -> Tuple[int]:
    return v.get_selected_tree_item_indexes(WidgetNames.tree_card_actions)


def get_card_name(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_card_name)


def get_action_name(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_name)


def get_action_owner_name(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_owner)


def get_action_is_done_or_not(v: ViewABC) -> bool:
    return v.get_value(WidgetNames.check_button_action_done)


def get_action_description(v: ViewABC) -> str:
    return v.get_value(WidgetNames.text_box_action_description)


def get_action_time_expected(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_time_expected)


def get_dead_line_str(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_dead_line)


def get_client(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_card_client)
