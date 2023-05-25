import datetime
from typing import Callable

import Utilities
import WidgetNames as wn
from GUI.list_of_actions import constants as c
from interface_view import ViewABC


def decide_text_color(action_id, v: ViewABC):
    if v.get_value(f'{c.CB_SCHEDULED}{action_id}'):
        color = c.SCHEDULED_COLOR
    else:
        color = c.DEFAULT_COLOR
    return color


def upon_cancel(v: ViewABC):
    close(v)


def close(v):
    v.close(c.POPUP)


def upon_ok(v: ViewABC, callback: Callable[[dict], None], data: dict):
    apply(v, callback, data)
    close(v)


def revert_all(v: ViewABC, data: dict):
    for card_state in data[c.KEY_CARD_STATES]:
        cs = card_state
        for action_id, done_or_not, scheduled, date in zip(
                cs[c.KEY_ACTION_IDS], cs[c.KEY_DONE_OR_NOT], cs[c.KEY_SCHEDULED], cs[c.KEY_DUE_DATES]):
            revert_action(action_id, date, done_or_not, scheduled, v, data)

    set_initial_label_appearances(v, data)


def set_duration(action_id, v: ViewABC, ask_user_for_duration: Callable, data: dict):
    def callback(duration: datetime.timedelta):
        v.set_value(f'{c.ENTRY_DURATION}{action_id}', duration)
        set_initial_label_appearances(v, data)

    ask_user_for_duration(callback)


def revert_action(action_id, date: str, done_or_not: bool, scheduled: bool, v: ViewABC, data: dict):
    v.set_value(f'{c.CB_DONE}{action_id}', done_or_not)
    v.set_value(f'{c.CB_SCHEDULED}{action_id}', scheduled)
    v.set_value(f'{c.ENTRY_DD}{action_id}', date)
    update_label(v, action_id, decide_text_color(action_id, v), data)


def apply(v: ViewABC, callback: Callable[[dict], None], data: dict):
    kwargs = create_kwargs_state(data, v)
    callback(**kwargs)


def create_kwargs_state(data: dict, v: ViewABC) -> dict:
    state = []
    for card_state in data[c.KEY_CARD_STATES]:
        for action_id in card_state[c.KEY_ACTION_IDS]:
            action_state = (
                action_id,
                v.get_value(f'{c.ENTRY_DD}{action_id}'),
                v.get_value(f'{c.CB_DONE}{action_id}'),
                v.get_value(f'{c.OWNER}{action_id}'),
                Utilities.time_delta_str_to_time_delta(v.get_value(f'{c.ENTRY_DURATION}{action_id}')),
                v.get_value(f'{c.CB_SCHEDULED}{action_id}')
            )
            state.append(action_state)
    kwargs = {c.KEY_KW_STATES: tuple(state)}
    return kwargs


def update_title_label(v: ViewABC, text: str):
    v.set_value(c.LABEL_TITLE, text)


def update_label(v: ViewABC, action_id_: str, color: str, data: dict):
    v.change_label_text_color(f'{c.ACTION_NAME}{action_id_}', color)

    kw = {
        'size': c.SELECTION_FONT_SIZE if not decide_overstrike(action_id_, v, data) else 13,
        'overstrike': decide_overstrike(action_id_, v, data)
    }
    v.change_label_font_size(f'{c.ACTION_NAME}{action_id_}', **kw)


def set_initial_label_appearances(v: ViewABC, data: dict):
    total_duration = datetime.timedelta(seconds=0)
    total_scheduled_duration = datetime.timedelta(seconds=0)
    action_counter = 0
    for card_state in data[c.KEY_CARD_STATES]:
        for action_id in card_state[c.KEY_ACTION_IDS]:
            color = decide_text_color(action_id, v)
            update_label(v, action_id, color, data)

            action_counter += 1
            duration_str = v.get_value(f'{c.ENTRY_DURATION}{action_id}')
            try:
                duration = Utilities.time_delta_str_to_time_delta(duration_str)
            except:
                duration = datetime.timedelta(seconds=0)
                v.set_value(f'{c.ENTRY_DURATION}{action_id}', duration)
            if v.get_value(f'{c.CB_SCHEDULED}{action_id}'):
                total_scheduled_duration += duration
            total_duration += duration

    tsd = total_scheduled_duration
    title_text = f'{action_counter} actions, total duration {total_duration}, of which {tsd} scheduled.'
    update_title_label(v, title_text)


def decide_overstrike(action_id_, v: ViewABC, data: dict) -> bool:
    return v.get_value(f'{c.CB_DONE}{action_id_}') or date_changed(action_id_, v, data)


def date_changed(action_id_, v: ViewABC, data: dict) -> bool:
    datetime_entry = Utilities.str_to_date_time_no_time(v.get_value(f'{c.ENTRY_DD}{action_id_}'))
    datetime_today = data[c.KEY_DATE]
    return datetime_entry > datetime_today


def upon_increment_button(v: ViewABC, shift: int, action_id, data: dict):
    increment_date(v, shift, action_id)
    update_label(v, action_id, c.SELECTION_COLOR, data)


def increment_date(v: ViewABC, shift: int, action_id):
    widget_id = f'{c.ENTRY_DD}{action_id}'
    current_date = Utilities.str_to_date_time_no_time(v.get_value(widget_id))
    new_date = current_date + datetime.timedelta(shift)
    v.set_value(f'{c.ENTRY_DD}{action_id}', Utilities.datetime_to_str_no_time(new_date))


def upon_right_click(v: ViewABC, callback, data: dict, action_id):
    kwargs = create_kwargs_state(data, v)
    kwargs.update(
        {
            c.KEY_KW_OPEN_RESOURCE: action_id,
            c.KEY_KW_OPEN_RESOURCE_METHOD: lambda: v.select_note_book_tab(wn.notebook_actions, 2)
        })
    callback(**kwargs)
    close(v)
