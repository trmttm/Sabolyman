import GUI.list_of_actions.constants as c
from GUI.list_of_actions import list_of_actions
from interface_tk import top_level_options
from interface_tk import widget_model as wm
from interface_view import ViewABC


def execute(v: ViewABC, data: dict, commands: dict):
    pop_up_list_of_resources(data, v, commands)


def pop_up_list_of_resources(data: dict, view: ViewABC, callback: dict):
    options = top_level_options('List of Resources', (1500, 800))
    view_model = [wm('root', c.POPUP, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += list_of_actions.get_view_model(c.POPUP, data)
    view.add_widgets(view_model)

    list_of_actions.bind_commands(view, callback, data)
