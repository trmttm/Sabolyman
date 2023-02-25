import datetime
from typing import Callable

from interface_tk import widget_model
from interface_view import ViewABC

file_name = 'datetime_setter.gui'
specified_parent = 'datetime_setter_parent'


def execute(v: ViewABC, view_model_passed: str, callback: Callable = None, **kwargs):
    parent_widget = 'toplevel'
    view_model = [widget_model('root', specified_parent, parent_widget, 0, 0, 0, 0, 'nswe', **{'geometry': '400x150'
        , 'title': kwargs.get('title', 'Set Date Time')})]
    view_model += view_model_passed

    v.add_widgets(view_model)
    bind_command(v, callback)


def bind_command(view: ViewABC, callback: Callable = None):
    d = datetime.datetime.today()
    d = datetime.datetime(d.year, d.month,d.day, d.hour, 0)
    if callback is None:
        callback = print

    def clear_datetime():
        nonlocal d
        d = datetime.datetime.today()
        d = datetime.datetime(d.year, d.month, d.day, d.hour, 0)
        update_label(d)

    def increment_year(year: int):
        nonlocal d
        try:
            d = d.replace(year=d.year + year)
        except ValueError:
            d = d.replace(year=d.year + year, day=d.day - 1)
        update_label(d)

    def increment_month(month: int):
        nonlocal d
        if d.month + month == 13:
            d = d.replace(year=d.year + 1, month=1)
        elif d.month + month == 0:
            d = d.replace(year=d.year - 1, month=12)
        elif d.month + month == 1:
            try:
                d = d.replace(month=d.month + month)
            except ValueError:
                d = d.replace(month=d.month + month, day=28)
        else:
            try:
                d = d.replace(month=d.month + month)
            except ValueError:
                d = d.replace(day=1)
                d = d.replace(month=d.month + month)
                find_last_valid_date_of_month()
        update_label(d)

    def increment_day(day: int):
        nonlocal d
        try:
            d = d.replace(day=d.day + day)
        except ValueError:
            d = d.replace(day=1)
            if day > 0:
                increment_month(1)
            else:
                increment_month(-1)
                find_last_valid_date_of_month()

        update_label(d)

    def find_last_valid_date_of_month():
        nonlocal d
        try:
            d = d.replace(day=31)
        except ValueError:
            try:
                d = d.replace(day=30)
            except ValueError:
                try:
                    d = d.replace(day=29)
                except ValueError:
                    d = d.replace(day=28)

    def increment_hour(hours: int):
        nonlocal d
        d += datetime.timedelta(seconds=hours * 60 * 60)
        update_label(d)

    def increment_minutes(minutes: int):
        nonlocal d
        d += datetime.timedelta(seconds=minutes * 60)
        update_label(d)

    def update_label(d: datetime.datetime):
        t = f'{d.year}/{d.month}/{d.day} {d.hour}:{d.minute}'
        view.set_value('lbl_datetime_display', t)

    def upon_ok(datetime_: datetime.datetime):
        view.close('datetime_setter_parent')
        callback(datetime_)

    view.bind_command_to_widget('btn_Y+', lambda: increment_year(1))
    view.bind_command_to_widget('btn_Y-', lambda: increment_year(-1))
    view.bind_command_to_widget('btn_M+', lambda: increment_month(1))
    view.bind_command_to_widget('btn_M-', lambda: increment_month(-1))
    view.bind_command_to_widget('btn_D+', lambda: increment_day(1))
    view.bind_command_to_widget('btn_D-', lambda: increment_day(-1))
    view.bind_command_to_widget('btn_H+', lambda: increment_hour(1))
    view.bind_command_to_widget('btn_H-', lambda: increment_hour(-1))
    view.bind_command_to_widget('btn_Min+', lambda: increment_minutes(5))
    view.bind_command_to_widget('btn_Min-', lambda: increment_minutes(-5))
    view.bind_command_to_widget('btn_clear', lambda: clear_datetime())
    view.bind_command_to_widget('btn_OK', lambda: upon_ok(d))
    update_label(d)
