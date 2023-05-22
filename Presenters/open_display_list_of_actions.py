from typing import Callable

import GUI
from interface_tk import top_level_options
from interface_tk import widget_model as wm
from interface_view import ViewABC


def execute(v: ViewABC, data: dict, callback: Callable[[dict], None]):
    pop_up_list_of_actions(data, v, callback)


def pop_up_list_of_actions(data: dict, view: ViewABC, callback: Callable[[dict], None]):
    options = top_level_options('List of Actions', (1000, 800))
    view_model = [wm('root', GUI.list_of_actions.POPUP, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += GUI.list_of_actions.get_view_model(GUI.list_of_actions.POPUP, data)
    view.add_widgets(view_model)

    GUI.list_of_actions.bind_commands(view, callback, data)
