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
