from typing import Tuple

import WidgetNames
from interface_view import ViewABC


def get_left_tree_selected_indexes(v: ViewABC) -> Tuple[int, ...]:
    return v.get_selected_tree_item_indexes(WidgetNames.tree_my_cards)


def get_right_tree_selected_indexes(v: ViewABC) -> Tuple[int, ...]:
    return v.get_selected_tree_item_indexes(WidgetNames.tree_their_cards)


def get_trees_selected_indexes(v: ViewABC) -> Tuple[Tuple[int, ...], ...]:
    indexes1 = get_left_tree_selected_indexes(v)
    indexes2 = get_right_tree_selected_indexes(v)
    return indexes1, indexes2


def get_actions_selected_indexes(v: ViewABC) -> Tuple[int]:
    return v.get_selected_tree_item_indexes(WidgetNames.tree_card_actions)


def get_action_resources_selected_indexes(v: ViewABC) -> Tuple[int]:
    return v.get_selected_tree_item_indexes(WidgetNames.tree_action_resources)


def get_card_name(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_card_name)


def get_action_name(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_name)


def get_action_owner_name(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_owner)


def get_action_is_done_or_not(v: ViewABC) -> bool:
    return v.get_value(WidgetNames.check_button_action_done)


def get_action_scheduled_or_not(v: ViewABC) -> bool:
    return v.get_value(WidgetNames.check_button_action_scheduled)


def get_action_description(v: ViewABC) -> str:
    return v.get_value(WidgetNames.text_box_action_description)


def get_action_time_expected(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_time_expected)


def get_dead_line_str(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_dead_line)


def get_start_from_str(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_start_from)


def get_client(v: ViewABC) -> str:
    return v.get_value(WidgetNames.entry_action_client)
