import datetime
from typing import Callable

from interface_tk import widget_model
from interface_view import ViewABC

file_name = 'minutes_setter.gui'
specified_parent = 'minute_setter_parent'


def execute(v: ViewABC, view_model_passed: str, callback: Callable = None, **kwargs):
    parent_widget = 'toplevel'
    view_model = [widget_model('root', specified_parent, parent_widget, 0, 0, 0, 0, 'nswe', **{'geometry': '250x100'
        , 'title': kwargs.get('title', 'Set Minutes')})]
    view_model += view_model_passed

    v.add_widgets(view_model)
    bind_command(v, callback)


def bind_command(view: ViewABC, callback: Callable = None):
    d = datetime.timedelta()
    if callback is None:
        callback = print

    def clear_minutes():
        nonlocal d
        d = datetime.timedelta()
        update_label(d)

    def increment_minutes(minutes: int):
        nonlocal d
        d += datetime.timedelta(seconds=minutes * 60)
        update_label(d)

    def update_label(timedelta: datetime.timedelta):
        view.set_value('lbl_minutes', timedelta)

    def upon_ok(timedelta: datetime.timedelta):
        view.close('minute_setter_parent')
        callback(timedelta)

    view.bind_command_to_widget('btn_05', lambda: increment_minutes(5))
    view.bind_command_to_widget('btn_10', lambda: increment_minutes(10))
    view.bind_command_to_widget('btn_15', lambda: increment_minutes(15))
    view.bind_command_to_widget('btn_30', lambda: increment_minutes(30))
    view.bind_command_to_widget('btn_60', lambda: increment_minutes(60))
    view.bind_command_to_widget('btn_clear', lambda: clear_minutes())
    view.bind_command_to_widget('btn_OK', lambda: upon_ok(d))
