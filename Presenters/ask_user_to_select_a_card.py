from typing import Callable

from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

specified_parent = 'popup_ask_for_a_parent'
button_ok = 'btn_ask_date_ok'


def execute(v: ViewABC, card_name_to_id: dict, callback: Callable):
    title = 'Select a parent card'
    width = 300
    height = 300

    stacker = Stacker(specified_parent)
    stacker.vstack(
        *tuple(w.Button(f'btn_parent_{n}').text(parent_name).command(
            lambda id_=parent_id: wrapped_callback(id_, callback, v)
        ) for (n, (parent_name, parent_id)) in enumerate(card_name_to_id.items())),
        w.Spacer(),
    )
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += stacker.view_model
    v.add_widgets(view_model)


def wrapped_callback(parent_id, callback: Callable, v: ViewABC):
    callback(parent_id)
    v.close(specified_parent)
