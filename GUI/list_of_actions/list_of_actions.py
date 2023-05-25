from typing import Callable

import GUI.list_of_actions.commands as cmd
import GUI.list_of_actions.gui_components as components
from GUI.list_of_actions.bind_events import bind_card_widgets
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

from . import constants as c


def get_view_model(parent: str = 'root', data: dict = None):
    if data is None:
        data = {}
    stacker = create_stacker(parent, data)
    view_model = stacker.view_model
    return view_model


def create_stacker(parent, data: dict):
    stacker = Stacker(specified_parent=parent)
    stacker.vstack(
        components.TITLE_LABEL(stacker),
        components.SCROLLABLE(data, stacker),
        components.BUTTOM_BUTTONS(stacker),
        w.Spacer().adjust(-2),
    )
    return stacker


def bind_commands(v: ViewABC, callback: Callable[[dict], None], data: dict):
    bind_card_widgets(v, callback, data)
    v.bind_command_to_widget(c.BTN_ACTIONS_CANCEL, lambda: cmd.upon_cancel(v))
    v.bind_command_to_widget(c.BTN_REPLACE, lambda: cmd.ask_user_what_to_replace(v, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_REVERT_ALL, lambda: cmd.revert_all(v, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_APPLY, lambda: cmd.apply(v, callback, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_OK, lambda: cmd.upon_ok(v, callback, data))

    cmd.set_initial_label_appearances(v, data)
