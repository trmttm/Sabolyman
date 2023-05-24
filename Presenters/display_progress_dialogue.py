import datetime
from typing import Callable

from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

specified_parent = 'popup_display_progress_dialogue'
button_ok = 'btn_display_progress_ok'


def execute(v: ViewABC, method_upon_ok: Callable = None, **kwargs):
    title = 'Pick Date Range' if kwargs.get('title') is None else kwargs.get('title')
    width = 600
    height = 120
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    day = today.day
    from_date_text = f'{year}/{month}/{day}' if kwargs.get('from') is None else kwargs.get('from')
    to_date_text = f'{year}/{month}/{day}' if kwargs.get('to') is None else kwargs.get('to')

    stacker = Stacker(specified_parent)
    stacker.vstack(
        stacker.hstack(
            w.Label('lbl_from').text('From'),
            w.Entry('entry_from').default_value(from_date_text).padding(10, 0)
        ),
        stacker.hstack(
            w.Label('lbl_to').text('To'),
            w.Entry('entry_to').default_value(to_date_text).padding(10, 0)
        ),
        w.Spacer(),
        stacker.hstack(
            w.Spacer(),
            w.Button('btn_display_progress_cancel').text("Cancel").padding(10, 10),
            w.Button(button_ok).text("OK").padding(10, 10),
        ),
        w.Spacer(),
    )
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += stacker.view_model
    v.add_widgets(view_model)

    v.bind_command_to_widget(specified_parent, lambda: v.close(specified_parent))
    v.bind_command_to_widget('btn_display_progress_cancel', lambda: v.close(specified_parent))
    v.focus(button_ok)

    if method_upon_ok is not None:
        def wrapper_to_delay_getting_entry_values():
            kwargs = {'from_': v.get_value('entry_from'), 'to_': v.get_value('entry_to')}
            method_upon_ok(**kwargs)
            v.close(specified_parent)

        v.bind_command_to_widget(button_ok, wrapper_to_delay_getting_entry_values)
