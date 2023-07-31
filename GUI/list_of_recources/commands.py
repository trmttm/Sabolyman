import Utilities
from GUI.list_of_recources import constants as c
from interface_view import ViewABC


def get_selected_paths(v: ViewABC):
    return tuple(v[-1] for v in v.tree_selected_values(c.TREE))


def open_files(paths, commands: dict):
    for path in paths:
        commands[c.CMD_OPEN_FILE](path)


def open_folders(paths, commands: dict):
    for path in paths:
        commands[c.CMD_OPEN_FOLDER](path)


def upon_heading_click(n: int, data: tuple, v: ViewABC):
    cards, actions, resources, extensions, paths = data
    if n == 1:
        update_tree(data, v)
    elif n > 1:
        index_ = n - 2
        sort_key = data[index_]
        _, sorted_cards = Utilities.sort_lists(sort_key, cards)
        _, sorted_actions = Utilities.sort_lists(sort_key, actions)
        _, sorted_resources = Utilities.sort_lists(sort_key, resources)
        _, sorted_extensions = Utilities.sort_lists(sort_key, extensions)
        _, sorted_paths = Utilities.sort_lists(sort_key, paths)

        sorted_data = sorted_cards, sorted_actions, sorted_resources, sorted_extensions, sorted_paths
        update_tree(sorted_data, v)


def update_tree(data, v: ViewABC):
    v.switch_tree(c.TREE)
    headings = c.TREE_HEADINGS
    widths = 50, 150, 150, 250, 50, 250
    tree_datas = tuple(Utilities.create_tree_data('', n, '', (n, crd, a, r, ex, p), (), False)
                       for (n, (crd, a, r, ex, p)) in enumerate(zip(*data)))
    stretches = False, False, False, False, True
    scroll_v = True
    scroll_h = True
    view_model = Utilities.create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)
    v.update_tree(view_model)
