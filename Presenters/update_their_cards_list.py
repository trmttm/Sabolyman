from typing import Tuple

import WidgetNames
from interface_view import ViewABC

from .update_cards_list import update_cards_list


def execute(v: ViewABC, sort_by: str, sorter_values: tuple, names: tuple, select_indexes: Tuple[int, ...], **kwargs):
    update_cards_list(v, names, sort_by, sorter_values, select_indexes, WidgetNames.tree_their_cards, **kwargs)
