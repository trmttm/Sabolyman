from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC

import WidgetNames


def execute(v: ViewABC, second_column_data: tuple, names: Tuple[str, ...], select_indexes: Tuple[int, ...], **kwargs):
    v.switch_tree(WidgetNames.tree_card_actions)
    view_model = create_view_model(second_column_data, names, select_indexes, **kwargs)
    v.update_tree(view_model)


def create_view_model(second_column_data: tuple, names: Tuple[str, ...], select_indexes: Tuple[int, ...], **kwargs):
    headings = 'No', 'Name', 'Completed'
    widths = 40, 100, 130
    tree_datas = []
    states: Tuple[bool, ...] = kwargs.get('states', tuple(False for _ in names))
    bgcs: Tuple[str, ...] = kwargs.get('back_ground_colors', tuple('White' for _ in names))
    text_colors = kwargs.get('text_colors', tuple(False for _ in names))
    z = zip(names, second_column_data, states, bgcs, text_colors)
    for n, (name, time_expected, state, background_color, text_color) in enumerate(z):
        time_expected_str = str(time_expected)
        tree_datas.append(
            create_tree_data('', f'{n}', '', (n, name, time_expected_str), (), n in select_indexes,
                             foreground=text_color, strikethrough=state, background=background_color)
        )
    stretches = False, True, False
    scroll_v = True
    scroll_h = True
    view_model = create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)
    return view_model
