import WidgetNames
from stacker import Stacker, widgets as w


def TREE_RESOURCES(stacker: Stacker):
    wn = WidgetNames
    return stacker.vstack(
        w.TreeView(wn.tree_action_resources),
        w.Label('spacer_to_prevent_scroll_bar_buttons_overlap').text(''),
        stacker.hstack(
            w.Spacer(),
            w.Button(wn.button_delete_selected_resources).text('X').width(1),
            w.Button(wn.button_move_down_selected_resources).text('↓').width(1),
            w.Button(wn.button_move_up_selected_resources).text('↑').width(1),
            w.Button(wn.button_add_new_resources).text('+').width(1),
            w.Button(wn.button_open_resource_folders).text('Folder').width(6),
            w.Button(wn.button_open_resources).text('Open').width(4),
            w.Spacer(),
        ),
    )
