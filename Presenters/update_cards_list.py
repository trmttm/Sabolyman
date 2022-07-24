from typing import Tuple

from interface_view import ViewABC

from . import create_view_model


def update_cards_list(v: ViewABC, names: tuple, sort_by: str, sort_by_values: tuple, select_indexes: Tuple[int, ...],
                      tree: str, **kwargs):
    headings = 'No', 'Name', sort_by
    v.switch_tree(tree)
    view_model = create_view_model.execute(headings, sort_by_values, names, select_indexes, **kwargs)
    v.update_tree(view_model)
    v.set_tree_headings(tree, headings)
