import Utilities
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
    stacker.vstack(
        w.TreeView(c.TREE),
        w.Label(c.BLANK_LABEL).text(''),
        stacker.hstack(
            w.Spacer(),
            w.Button(c.BTN_CLOSE).text('Close').padding(0, 10),
            w.Button(c.BTN_FOLDER).text('Folder').padding(5, 10),
            w.Button(c.BTN_OPEN).text('Open').padding(0, 10),
            w.Spacer(),
        ),
    )
    return stacker


def bind_commands(v: ViewABC, data: tuple, commands: dict):
    update_tree(data, v)
    v.bind_command_to_widget(c.POPUP, lambda: v.close(c.POPUP))
    v.bind_command_to_widget(c.BTN_CLOSE, lambda: v.close(c.POPUP))
    v.bind_command_to_widget(c.BTN_FOLDER, lambda: cmd.open_folders(cmd.get_selected_paths(v), commands))
    v.bind_command_to_widget(c.BTN_OPEN, lambda: cmd.open_files(cmd.get_selected_paths(v), commands))


def update_tree(data, v: ViewABC):
    v.switch_tree(c.TREE)
    cards, actions, resources, extensions, paths = data
    headings = 'No', 'Card', 'Action', 'Resource', 'Extension', 'Path'
    widths = 50, 150, 150, 250, 50, 250
    tree_datas = tuple(Utilities.create_tree_data('', n, '', (n, crd, a, r, ex, p), (), False)
                       for (n, (crd, a, r, ex, p)) in enumerate(zip(cards, actions, resources, extensions, paths)))
    stretches = False, False, False, False, True
    scroll_v = True
    scroll_h = True
    view_model = Utilities.create_view_model_tree(headings, widths, tree_datas, stretches, scroll_v, scroll_h)
    v.update_tree(view_model)
