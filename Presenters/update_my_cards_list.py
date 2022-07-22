from typing import Tuple

from interface_view import ViewABC

import WidgetNames
from .update_cards_list import update_cards_list


def execute(v: ViewABC, sort_by_values: tuple, names: tuple, select_indexes: Tuple[int, ...], **kwargs):
    update_cards_list(v, names,'Due Date', sort_by_values, select_indexes, WidgetNames.tree_my_cards, **kwargs)
