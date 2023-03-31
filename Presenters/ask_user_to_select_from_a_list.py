from typing import Callable

from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

specified_parent = 'popup_ask_to_choose_from_a_list'


def execute(v: ViewABC, display_to_data: dict, callback: Callable):
    title = 'Select a parent card'
    width = 300
    height = 300

    stacker = Stacker(specified_parent)
    stacker.vstack_scrollable(
        *tuple(w.Button(f'btn_parent_{n}').text(parent_name).command(
            lambda id_=parent_id: wrapped_callback(id_, callback, v)
        ) for (n, (parent_name, parent_id)) in enumerate(display_to_data.items())),
        w.Spacer(),
    )
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += stacker.view_model
    v.add_widgets(view_model)

    v.bind_command_to_widget(specified_parent, lambda: v.close(specified_parent))


def wrapped_callback(parent_id, callback: Callable, v: ViewABC):
    callback(parent_id)
    v.close(specified_parent)
