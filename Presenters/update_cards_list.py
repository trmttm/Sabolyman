from typing import Tuple

from interface_view import ViewABC

from . import create_view_model
from .utilities import datetime_to_str


def update_cards_list(v: ViewABC, names: tuple, sort_by_values: tuple, select_indexes: Tuple[int, ...], tree: str,
                      **kwargs):
    v.switch_tree(tree)
    view_model = get_view_model_sort_by_due_dates(names, sort_by_values, select_indexes, kwargs)
    v.update_tree(view_model)


def get_view_model_sort_by_due_dates(names, sort_by_values, select_indexes, kwargs):
    due_dates_str = tuple(datetime_to_str(d) for d in sort_by_values)
    view_model = create_view_model.execute('Due Date', due_dates_str, names, select_indexes, **kwargs)
    return view_model
