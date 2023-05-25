import datetime
from typing import Callable

import Utilities
import WidgetNames as wn
from GUI import ask_user_for_entries
from . import constants as c
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w


def get_view_model(parent: str = 'root', data: dict = None):
    if data is None:
        data = {}
    stacker = create_stacker(parent, data)
    view_model = stacker.view_model
    return view_model


def create_stacker(parent, data: dict):
    stacker = Stacker(specified_parent=parent)
    stacker.vstack(
        stacker.hstack(
            w.Spacer(),
            w.Label(c.LABEL_TITLE).text('Title').padding(0, 20),
            w.Spacer(),
        ),
        stacker.vstack_scrollable(
            *ALL_CARDS_WIDGETS(stacker, data)
        ),
        stacker.hstack(
            w.Spacer(),
            w.Button(c.BTN_ACTIONS_CANCEL).text('Cancel').padding(5, 10),
            w.Button(c.BTN_REPLACE).text('Replace').padding(5, 10),
            w.Button(c.BTN_ACTIONS_REVERT_ALL).text('Revert All').padding(5, 10),
            w.Button(c.BTN_ACTIONS_APPLY).text('Apply').padding(5, 10),
            w.Button(c.BTN_ACTIONS_OK).text('Done').padding(5, 10),
            w.Spacer(),
        ),
        w.Spacer().adjust(-2),
    )
    return stacker


def ALL_CARDS_WIDGETS(stacker, data: dict) -> tuple:
    card_widgets = ()
    for n, card_state in enumerate(data[c.KEY_CARD_STATES]):
        card_widgets += CARD_WIDGETS(stacker, n, data)
    return card_widgets


def CARD_WIDGETS(stacker, n: int, data: dict):
    return (
        w.Label('blank').text(''),
        w.Label(f'card_name_{n}').text(data[c.KEY_CARD_STATES][n][c.CARD_NAME]).padding(c.CARD_PADX, 0),

    ) + ACTION_WITHIN_A_CARD(stacker, data[c.KEY_CARD_STATES][n])


def ACTION_WITHIN_A_CARD(stacker, action_state):
    return tuple(
        stacker.hstack(
            w.Label(f'{c.ACTION_NAME}{action_id}').text(action_state.get(c.KEY_NAMES, ())[n]).padding(c.ACTION_PADX, 0),
            w.Entry(f'{c.OWNER}{action_id}').default_value(f'{owner}'),
            w.Button(f'{c.BTN_DD_DOWN}{action_id}').text('↓').width(2),
            w.Entry(f'{c.ENTRY_DD}{action_id}').default_value(action_state.get(c.KEY_DUE_DATES, ())[n]),
            w.Button(f'{c.BTN_DD_UP}{action_id}').text('↑').width(2),
            w.Label(f'label_done{action_id}').text('D').width(2),
            w.CheckButton(f'{c.CB_DONE}{action_id}').value(action_state.get(c.KEY_DONE_OR_NOT, ())[n]),
            w.Label(f'label_scheduled{action_id}').text('S').width(2),
            w.CheckButton(f'{c.CB_SCHEDULED}{action_id}').value(action_state.get(c.KEY_SCHEDULED, ())[n]),
            w.Entry(f'{c.ENTRY_DURATION}{action_id}').default_value(action_state.get(c.KEY_DURATION, ())[n]).width(10),
            w.Button(f'{c.BTN_SET_DURATION}{action_id}').text('+').width(2),
            w.Button(f'{c.BTN_REVERT}{action_id}').text('↩︎').width(2),
            w.Spacer().adjust(-12),
        ) for (n, (action_id, owner)) in
        enumerate(zip(action_state.get(c.KEY_ACTION_IDS, ()), action_state.get(c.KEY_OWNERS, ()), ))
    )


def update_title_label(v: ViewABC, text: str):
    v.set_value(c.LABEL_TITLE, text)


def update_label(v: ViewABC, action_id_: str, color: str, data: dict):
    v.change_label_text_color(f'{c.ACTION_NAME}{action_id_}', color)

    kw = {
        'size': c.SELECTION_FONT_SIZE if not decide_overstrike(action_id_, v, data) else 13,
        'overstrike': decide_overstrike(action_id_, v, data)
    }
    v.change_label_font_size(f'{c.ACTION_NAME}{action_id_}', **kw)


def decide_overstrike(action_id_, v: ViewABC, data: dict) -> bool:
    return v.get_value(f'{c.CB_DONE}{action_id_}') or date_changed(action_id_, v, data)


def date_changed(action_id_, v: ViewABC, data: dict) -> bool:
    datetime_entry = Utilities.str_to_date_time_no_time(v.get_value(f'{c.ENTRY_DD}{action_id_}'))
    datetime_today = data[c.KEY_DATE]
    return datetime_entry > datetime_today


def bind_commands(v: ViewABC, callback: Callable[[dict], None], data: dict):
    bind_card_widgets(v, callback, data)
    v.bind_command_to_widget(c.BTN_ACTIONS_CANCEL, lambda: upon_cancel(v))
    v.bind_command_to_widget(c.BTN_REPLACE, lambda: ask_user_what_to_replace(v, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_REVERT_ALL, lambda: revert_all(v, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_APPLY, lambda: apply(v, callback, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_OK, lambda: upon_ok(v, callback, data))

    set_initial_label_appearances(v, data)


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


def close(v):
    v.close(c.POPUP)


def upon_cancel(v: ViewABC):
    close(v)


def ask_user_what_to_replace(v: ViewABC, data: dict):
    def callback(user_entries: tuple[str, ...]):
        from_, to_, also_replace_earlier_dates = user_entries
        datetime_from = Utilities.str_to_date_time_no_time(from_)
        datetime_to = Utilities.str_to_date_time_no_time(to_)
        counter = 0
        for card_state in data[c.KEY_CARD_STATES]:
            for action_id, action_name in zip(card_state[c.KEY_ACTION_IDS], card_state[c.KEY_NAMES]):
                entry_id = f'{c.ENTRY_DD}{action_id}'
                datetime_str_current = v.get_value(entry_id)
                datetime_current = Utilities.str_to_date_time_no_time(datetime_str_current)
                datetime_current_with_time = Utilities.str_to_date_time(datetime_str_current)

                exact_match = datetime_current == datetime_from
                replace_earlier_datetime_also = also_replace_earlier_dates and (datetime_current <= datetime_from)
                if exact_match or replace_earlier_datetime_also:
                    d = datetime_to
                    dct = datetime_current_with_time
                    date_time_to_with_time = datetime.datetime(d.year, d.month, d.day, dct.hour, dct.minute)
                    to_with_time = Utilities.datetime_to_str(date_time_to_with_time)

                    v.set_value(entry_id, Utilities.datetime_to_str(date_time_to_with_time))
                    counter += 1
                    print(f'{counter} [{action_name}] due_date replaced from {datetime_str_current} to {to_with_time}')

    kwargs = {}
    kwargs['title'] = 'Replace date at once'
    kwargs['message'] = 'Specify what to replace with what'
    today = Utilities.datetime_to_str_no_time(datetime.datetime.today())
    kwargs['labels'] = ('Replace...', 'With...', 'Also replace earlier deadlines?')
    kwargs['check_button_index'] = (2,)
    kwargs['default_values'] = (today, today, False)
    ask_user_for_entries.execute(v, callback, **kwargs)


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


def bind_card_widgets(v: ViewABC, callback: Callable[[dict], None], data: dict):
    for card_state in data[c.KEY_CARD_STATES]:
        bind_each_card_widget(card_state, v, callback, data)


def bind_each_card_widget(card_state: dict, v: ViewABC, callback: Callable[[dict], None], data: dict):
    cs = card_state
    for id_, date, done_or_not, scheduled in zip(cs[c.KEY_ACTION_IDS], cs[c.KEY_DUE_DATES], cs[c.KEY_DONE_OR_NOT],
                                                 cs[c.KEY_SCHEDULED]):
        bind_action(id_, date, done_or_not, scheduled, v, callback, data)


def bind_action(action_id, date, done_or_not: bool, scheduled: bool, v: ViewABC, callback: Callable[[dict], None],
                data: dict):
    bind = v.bind_command_to_widget
    bind(f'{c.BTN_DD_DOWN}{action_id}', lambda i=action_id: upon_increment_button(v, -1, i, data))
    bind(f'{c.BTN_DD_UP}{action_id}', lambda i=action_id: upon_increment_button(v, 1, i, data))
    bind(f'{c.BTN_REVERT}{action_id}', lambda i=action_id: revert_action(i, date, done_or_not, scheduled, v, data))
    bind(f'{c.BTN_SET_DURATION}{action_id}', lambda i=action_id: set_duration(i, v, data[c.KEY_CB_DURATION], data))
    bind(f'{c.CB_DONE}{action_id}', lambda i=action_id: update_label(v, i, decide_text_color(action_id, v), data))
    bind(f'{c.ENTRY_DURATION}{action_id}', lambda *_: set_initial_label_appearances(v, data))
    bind(f'{c.CB_SCHEDULED}{action_id}', lambda *_: set_initial_label_appearances(v, data))
    bind_mouse_hover(action_id, v, data)

    entry_id = f'{c.ACTION_NAME}{action_id}'
    v.bind_left_click(lambda e: print(f'Right clicked {v.get_value(entry_id)}'), entry_id)
    v.bind_right_click(lambda e: upon_right_click(v, callback, data, action_id), entry_id)
    v.bind_middle_click(lambda e: print(f'Middle clicked {v.get_value(entry_id)}'), entry_id)


def bind_mouse_hover(action_id, v: ViewABC, data: dict):
    aid = action_id

    for key in (c.BTN_DD_UP, c.BTN_DD_DOWN, c.ENTRY_DD, c.CB_DONE, c.ACTION_NAME, c.OWNER, c.BTN_REVERT, c.CB_SCHEDULED):
        v.bind_mouse_enter(lambda i=aid: update_label(v, i, c.SELECTION_COLOR, data), f'{key}{aid}')
        v.bind_mouse_leave(lambda i=aid: update_label(v, i, decide_text_color(action_id, v), data), f'{key}{aid}')


def decide_text_color(action_id, v: ViewABC):
    if v.get_value(f'{c.CB_SCHEDULED}{action_id}'):
        color = c.SCHEDULED_COLOR
    else:
        color = c.DEFAULT_COLOR
    return color
