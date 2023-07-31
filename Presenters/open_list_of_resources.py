from GUI.list_of_recources import bind_commands
from GUI.list_of_recources import constants as c
from GUI.list_of_recources import get_view_model
from interface_tk import top_level_options
from interface_tk import widget_model as wm
from interface_view import ViewABC


def execute(v: ViewABC, data: tuple, commands: dict):
    pop_up_list_of_resources(data, v, commands)


def pop_up_list_of_resources(data: tuple, view: ViewABC, commands: dict):
    options = top_level_options('List of Resources', (1500, 800))
    view_model = [wm('root', c.POPUP, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += get_view_model(c.POPUP)
    view.add_widgets(view_model)

    bind_commands(view, data, commands)
