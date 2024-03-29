from typing import Callable

import os_identifier
from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

specified_parent = 'popup_ask_for_user_entry'
button_ok = 'user_input_ok'
entry_by_user = 'entry_by_user_'


def execute(v: ViewABC, callback: Callable, **kwargs):
    title = kwargs.get('title', 'User entry')
    message = kwargs.get('message', 'Enter value')
    default_values = kwargs.get('default_values', ('',))
    labels = kwargs.get('labels', tuple(n + 1 for n in range(len(default_values))))
    check_button_index = kwargs.get('check_button_index', ())
    width = 300
    height = 300

    stacker = Stacker(specified_parent)
    stacker.vstack_scrollable(
        w.Label('user_entry_body').text(message),
        *tuple(
            stacker.hstack(
                w.Label(f'label_{entry_by_user}{n}').text(label),
                ENTRY_OR_CHECKBUTTON(n, default_value, check_button_index),
                w.Spacer().adjust(-1),
            ) for (n, (label, default_value)) in enumerate(zip(labels, default_values))
        ),
        w.Button(button_ok).text('OK').padding(10, 10),
        w.Spacer(),
    )
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += stacker.view_model
    v.add_widgets(view_model)

    v.bind_command_to_widget(button_ok, lambda: upon_ok(v, len(default_values), callback))
    v.bind_command_to_widget(specified_parent, lambda: v.close(specified_parent))

    v.focus(f'{entry_by_user}{0}')


def ENTRY_OR_CHECKBUTTON(n, value, check_button_index: tuple):
    return ENTRY(n, value) if n not in check_button_index else CHECKBUTTON(n, value)


def ENTRY(n, value):
    v = value
    if os_identifier.DIRECTORY_SEPARATOR in value and '.' in value:
        v = value.split(os_identifier.DIRECTORY_SEPARATOR)[-1]
    return w.Entry(f'{entry_by_user}{n}').default_value(v)


def CHECKBUTTON(n, value):
    return w.CheckButton(f'{entry_by_user}{n}').value(value)


def upon_ok(v: ViewABC, number_of_entries: int, callback: Callable):
    user_input_values = tuple(v.get_value(f'{entry_by_user}{n}') for n in range(number_of_entries))
    callback(user_input_values)
    v.close(specified_parent)


def wrapped_callback(parent_id, callback: Callable, v: ViewABC):
    callback(parent_id)
    v.close(specified_parent)
