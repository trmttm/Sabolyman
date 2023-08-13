from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

from . import commands as cmd
from . import constants as c


def get_view_model(parent: str = 'root'):
    stacker = create_stacker(parent)
    view_model = stacker.view_model
    return view_model


def create_stacker(parent):
    stacker = Stacker(specified_parent=parent)
    LIST_OF_RESOURCES(stacker)
    return stacker


def LIST_OF_RESOURCES(stacker):
    return stacker.vstack(
        w.TreeView(c.TREE),
        w.Label(c.BLANK_LABEL).text(''),
        stacker.hstack(
            w.Spacer(),
            w.Button(c.BTN_CLOSE).text('Close').padding(0, 10),
            w.Button(c.BTN_CLEAR_SORT).text('Clear Sorter').padding(5, 10),
            w.Button(c.BTN_FOLDER).text('Folder').padding(5, 10),
            w.Button(c.BTN_OPEN).text('Open').padding(0, 10),
            w.Spacer(),
        ),
    )


def bind_commands(v: ViewABC, data: tuple, commands: dict):
    cmd.update_tree(data, v)
    v.bind_command_to_widget(c.POPUP, lambda: v.close(c.POPUP))
    v.bind_command_to_widget(c.BTN_CLOSE, lambda: v.close(c.POPUP))
    v.bind_command_to_widget(c.BTN_CLEAR_SORT, lambda: cmd.update_tree(data, v))
    v.bind_command_to_widget(c.BTN_FOLDER, lambda: cmd.open_folders(cmd.get_selected_paths(v), commands))
    v.bind_command_to_widget(c.BTN_OPEN, lambda: cmd.open_files(cmd.get_selected_paths(v), commands))
    v.bind_tree_click_heading(c.TREE, lambda col_n: cmd.upon_heading_click(col_n, data, v))
