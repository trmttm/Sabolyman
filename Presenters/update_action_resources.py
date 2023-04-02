from Utilities import create_tree_data
from Utilities import create_view_model_tree
from interface_view import ViewABC

import WidgetNames


def execute(v: ViewABC, names: tuple, **kwargs):
    tree = WidgetNames.tree_action_resources

    headings = 'No', 'Resource URI'
    v.switch_tree(tree)
    widths = 40, 100, 130
    tree_datas = []
    stretches = False, True
    scroll_v = True
    scroll_h = True

    strikethroughs = kwargs.get('strikethroughs', tuple(False for _ in names))
    colors = kwargs.get('colors', tuple(None for _ in names))
    underlines = kwargs.get('underlines', tuple(False for _ in names))
    bolds = kwargs.get('bolds', tuple(False for _ in names))
    text_colors = kwargs.get('text_colors', tuple('Black' for _ in names))

    z = zip(names, strikethroughs, colors, underlines, bolds, text_colors)
    select_indexes = ()
    for n, (name, strikethrough, color, underline, bold, text_color) in enumerate(z):
        tree_datas.append(create_tree_data('', f'{n}', '', (n, name), (), n in select_indexes,
                                           foreground=text_color, strikethrough=strikethrough, background=color,
                                           underline=underline, bold=bold))

    view_model = create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)

    v.update_tree(view_model)
    v.set_tree_headings(tree, headings)
