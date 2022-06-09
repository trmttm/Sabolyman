from typing import Tuple

from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC

from .utilities import datetime_to_str


def update_cards_list(v: ViewABC, names: tuple, due_dates: tuple, select_indexes: Tuple[int, ...], tree: str, **kwargs):
    v.switch_tree(tree)
    view_model = create_view_model(due_dates, names, select_indexes, **kwargs)
    v.update_tree(view_model)


def create_view_model(due_dates: tuple, names: tuple, select_indexes: Tuple[int, ...], **kwargs):
    headings = 'Name', 'Due Date'
    widths = 100, 130
    tree_datas = []
    all_status = kwargs.get('completions_status', tuple(False for _ in names))
    for n, (name, due_date, status) in enumerate(zip(names, due_dates, all_status)):
        due_date_str = datetime_to_str(due_date)
        tree_datas.append(create_tree_data('', f'{n}', '', (name, due_date_str), (), n in select_indexes,
                                           strikethrough=status))
    stretches = True, False
    scroll_v = True
    scroll_h = True
    view_model = create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)
    return view_model
