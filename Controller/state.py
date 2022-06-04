from typing import Tuple

from interface_view import ViewABC

import WidgetNames


def get_my_cards_selected_indexes(v: ViewABC) -> Tuple[int]:
    wn = WidgetNames
    return v.get_selected_tree_item_indexes(wn.tree_my_cards)


def get_card_name(v: ViewABC) -> str:
    wn = WidgetNames
    return v.get_value(wn.entry_card_name)


def get_dead_line_str(v: ViewABC) -> str:
    wn = WidgetNames
    return v.get_value(wn.entry_dead_line)
