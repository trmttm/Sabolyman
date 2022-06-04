from typing import Tuple

from interface_view import ViewABC


def get_my_balls_selected_indexes(v: ViewABC) -> Tuple[int]:
    return v.get_selected_tree_item_indexes('tree_my_balls')


def get_card_name(v: ViewABC) -> str:
    return v.get_value('entry_name')


def get_dead_line_str(v: ViewABC) -> str:
    return v.get_value('entry_dead_line')
