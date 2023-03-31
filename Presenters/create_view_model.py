from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree


def execute(headings: Tuple[str, ...], sorter_values: tuple, names: tuple, select_indexes: Tuple[int, ...], **kwargs):
    widths = 40, 100, 130
    tree_datas = []
    all_status = kwargs.get('completions_status', tuple(False for _ in names))
    colors = kwargs.get('colors', tuple(False for _ in names))
    bolds = kwargs.get('bolds', tuple(False for _ in names))
    text_colors = kwargs.get('text_colors', tuple(False for _ in names))
    z = zip(names, sorter_values, all_status, colors, bolds, text_colors)
    for n, (name, sort_by_value, status, color, bold, text_color) in enumerate(z):
        tree_datas.append(create_tree_data('', f'{n}', '', (n, name, sort_by_value), (), n in select_indexes,
                                           foreground=text_color, strikethrough=status, background=color, bold=bold))
    stretches = False, True, False
    scroll_v = True
    scroll_h = True
    view_model = create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)
    return view_model
