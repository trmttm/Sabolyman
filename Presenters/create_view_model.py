from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree


def execute(headings: Tuple[str, ...], sort_by_values: tuple, names: tuple, select_indexes: Tuple[int, ...], **kwargs):
    widths = 40, 100, 130
    tree_datas = []
    all_status = kwargs.get('completions_status', tuple(False for _ in names))
    colors = kwargs.get('colors', tuple(False for _ in names))
    for n, (name, sort_by_value, status, color) in enumerate(zip(names, sort_by_values, all_status, colors)):
        tree_datas.append(create_tree_data('', f'{n}', '', (n, name, sort_by_value), (), n in select_indexes,
                                           strikethrough=status, background=color))
    stretches = False, True, False
    scroll_v = True
    scroll_h = True
    view_model = create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)
    return view_model
