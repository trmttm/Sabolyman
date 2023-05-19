import datetime
from typing import Callable

import Utilities
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

POPUP = 'popup_list_of_actions'
CARD_NAME = 'card_name'
KEY_ACTION_IDS = 'action_ids'
KEY_NAMES = 'action_names'
KEY_DUE_DATES = 'action_due_dates'
KEY_DONE_OR_NOT = 'done_or_not'
BTN_ACTIONS_CANCEL = 'btn_actions_cancel'
BTN_ACTIONS_REVERT_ALL = 'btn_actions_revert'
BTN_ACTIONS_APPLY = 'btn_actions_apply'
BTN_ACTIONS_OK = 'btn_actions_ok'

BTN_DD_DOWN = 'button_due_date_down_'
BTN_DD_UP = 'button_due_date_up_'
BTN_REVERT = 'button_revert_'
ENTRY_DD = 'entry_due_date'
CB_DONE = 'done_or_not_'
NUMBER = 'number_'
ACTION_NAME = 'action_name_'
SELECTION_COLOR = 'red'
DEFAULT_COLOR = 'blue'
SELECTION_FONT_SIZE = 15

CARD_PADX = 20
ACTION_PADX = 40

KEY_CARD_STATES = 'card_states'
KEY_DATE = 'date'


def get_view_model(parent: str = 'root', data: dict = None):
    if data is None:
        data = {}
    stacker = create_stacker(parent, data)
    view_model = stacker.view_model
    return view_model


def create_stacker(parent, data: dict):
    stacker = Stacker(specified_parent=parent)
    stacker.vstack(
        stacker.vstack_scrollable(
            *ALL_CARDS_WIDGETS(stacker, data)
        ),
        stacker.hstack(
            w.Spacer(),
            w.Button(BTN_ACTIONS_CANCEL).text('Cancel').padding(5, 10),
            w.Button(BTN_ACTIONS_REVERT_ALL).text('Revert All').padding(5, 10),
            w.Button(BTN_ACTIONS_APPLY).text('Apply').padding(5, 10),
            w.Button(BTN_ACTIONS_OK).text('Done').padding(5, 10),
            w.Spacer(),
        )
    )
    return stacker


def ALL_CARDS_WIDGETS(stacker, data: dict) -> tuple:
    card_widgets = ()
    for n, card_state in enumerate(data[KEY_CARD_STATES]):
        card_widgets += CARD_WIDGETS(stacker, n, data)
    return card_widgets


def CARD_WIDGETS(stacker, n: int, data: dict):
    return (
               w.Label('blank').text(''),
               w.Label(f'card_name_{n}').text(data[KEY_CARD_STATES][n][CARD_NAME]).padding(CARD_PADX, 0),

           ) + ACTION_WITHIN_A_CARD(stacker, data[KEY_CARD_STATES][n])


def ACTION_WITHIN_A_CARD(stacker, action_state):
    return tuple(
        stacker.hstack(
            w.Label(f'{NUMBER}{action_id}').text(f'{action_id}').padding(ACTION_PADX, 1),
            w.Label(f'{ACTION_NAME}{action_id}').text(action_state.get(KEY_NAMES, ())[n]),
            w.Button(f'{BTN_DD_DOWN}{action_id}').text('↓').width(2),
            w.Entry(f'{ENTRY_DD}{action_id}').default_value(action_state.get(KEY_DUE_DATES, ())[n]).width(10),
            w.Button(f'{BTN_DD_UP}{action_id}').text('↑').width(2),
            w.CheckButton(f'{CB_DONE}{action_id}').value(action_state.get(KEY_DONE_OR_NOT, ())[n]).padding(20, 0),
            w.Button(f'{BTN_REVERT}{action_id}').text('Revert'),
            w.Spacer().adjust(-6),
        ) for (n, action_id) in enumerate(action_state.get(KEY_ACTION_IDS, ()))
    )


def update_label(v: ViewABC, action_id_: str, color: str, data: dict):
    v.change_label_text_color(f'{NUMBER}{action_id_}', color)
    v.change_label_text_color(f'{ACTION_NAME}{action_id_}', color)

    kw = {
        'size': SELECTION_FONT_SIZE if not decide_overstrike(action_id_, v, data) else None,
        'overstrike': decide_overstrike(action_id_, v, data)
    }
    v.change_label_font_size(f'{NUMBER}{action_id_}', **kw)
    v.change_label_font_size(f'{ACTION_NAME}{action_id_}', **kw)


def decide_overstrike(action_id_, v: ViewABC, data: dict) -> bool:
    return v.get_value(f'{CB_DONE}{action_id_}') or date_changed(action_id_, v, data)


def date_changed(action_id_, v: ViewABC, data: dict) -> bool:
    datetime_entry = Utilities.str_to_date_time_no_time(v.get_value(f'{ENTRY_DD}{action_id_}'))
    datetime_today = data[KEY_DATE]
    return datetime_entry > datetime_today


def bind_commands(v: ViewABC, callback: Callable[[tuple], None], data: dict):
    bind_card_widgets(v, data)
    v.bind_command_to_widget(BTN_ACTIONS_CANCEL, lambda: upon_cancel(v))
    v.bind_command_to_widget(BTN_ACTIONS_REVERT_ALL, lambda: revert_all(v, data))
    v.bind_command_to_widget(BTN_ACTIONS_APPLY, lambda: apply(v, callback, data))
    v.bind_command_to_widget(BTN_ACTIONS_OK, lambda: upon_ok(v, callback, data))

    set_initial_label_appearances(v, data)


def apply(v: ViewABC, callback: Callable[[tuple], None], data: dict):
    state = []
    for card_state in data[KEY_CARD_STATES]:
        for action_id in card_state[KEY_ACTION_IDS]:
            state.append((action_id, v.get_value(f'{ENTRY_DD}{action_id}'), v.get_value(f'{CB_DONE}{action_id}')))
    callback(tuple(state))


def close(v):
    v.close(POPUP)


def upon_cancel(v: ViewABC):
    close(v)


def upon_ok(v: ViewABC, callback: Callable[[tuple], None], data: dict):
    apply(v, callback, data)
    close(v)


def revert_all(v: ViewABC, data: dict):
    for card_state in data[KEY_CARD_STATES]:
        cs = card_state
        for action_id, done_or_not, date in zip(cs[KEY_ACTION_IDS], cs[KEY_DONE_OR_NOT], cs[KEY_DUE_DATES]):
            revert_action(action_id, date, done_or_not, v, data)

    set_initial_label_appearances(v, data)


def revert_action(action_id, date: str, done_or_not: bool, v: ViewABC, data: dict):
    v.set_value(f'{CB_DONE}{action_id}', done_or_not)
    v.set_value(f'{ENTRY_DD}{action_id}', date)
    update_label(v, action_id, DEFAULT_COLOR, data)


def upon_increment_button(v: ViewABC, shift: int, action_id, data: dict):
    increment_date(v, shift, action_id)
    update_label(v, action_id, SELECTION_COLOR, data)


def increment_date(v: ViewABC, shift: int, action_id):
    widget_id = f'{ENTRY_DD}{action_id}'
    current_date = Utilities.str_to_date_time_no_time(v.get_value(widget_id))
    new_date = current_date + datetime.timedelta(shift)
    v.set_value(f'{ENTRY_DD}{action_id}', Utilities.datetime_to_str_no_time(new_date))


def set_initial_label_appearances(v: ViewABC, data: dict):
    for card_state in data[KEY_CARD_STATES]:
        for action_id in card_state[KEY_ACTION_IDS]:
            update_label(v, action_id, DEFAULT_COLOR, data)


def bind_card_widgets(v: ViewABC, data: dict):
    for card_state in data[KEY_CARD_STATES]:
        bind_each_card_widget(card_state, v, data)


def bind_each_card_widget(card_state: dict, v: ViewABC, data: dict):
    cs = card_state
    for action_id, date, done_or_not in zip(cs[KEY_ACTION_IDS], cs[KEY_DUE_DATES], cs[KEY_DONE_OR_NOT]):
        bind_action(action_id, date, done_or_not, v, data)


def bind_action(action_id, date, done_or_not: bool, v: ViewABC, data: dict):
    bind = v.bind_command_to_widget
    bind(f'{BTN_DD_DOWN}{action_id}', lambda i=action_id: upon_increment_button(v, -1, i, data))
    bind(f'{BTN_DD_UP}{action_id}', lambda i=action_id: upon_increment_button(v, 1, i, data))
    bind(f'{BTN_REVERT}{action_id}', lambda i=action_id: revert_action(i, date, done_or_not, v, data))
    bind(f'{CB_DONE}{action_id}', lambda i=action_id: update_label(v, i, DEFAULT_COLOR, data))
    bind_mouse_hover(action_id, v, data)


def bind_mouse_hover(action_id, v: ViewABC, data: dict):
    aid = action_id

    for key in (BTN_DD_UP, BTN_DD_DOWN, ENTRY_DD, CB_DONE, ACTION_NAME, NUMBER):
        v.bind_mouse_enter(lambda i=aid: update_label(v, i, SELECTION_COLOR, data), f'{key}{aid}')
        v.bind_mouse_leave(lambda i=aid: update_label(v, i, DEFAULT_COLOR, data), f'{key}{aid}')
