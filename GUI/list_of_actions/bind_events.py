from typing import Callable

import GUI.list_of_actions.commands as cmd
from GUI.list_of_actions import constants as c
from interface_view import ViewABC


def bind_card_widgets(v: ViewABC, callback: Callable[[dict], None], data: dict):
    for card_state in data[c.KEY_CARD_STATES]:
        bind_each_card_widget(card_state, v, callback, data)


def bind_each_card_widget(card_state: dict, v: ViewABC, callback: Callable[[dict], None], data: dict):
    cs = card_state
    for id_, date, done_or_not, scheduled, duration in zip(
            cs[c.KEY_ACTION_IDS], cs[c.KEY_DUE_DATES], cs[c.KEY_DONE_OR_NOT], cs[c.KEY_SCHEDULED], cs[c.KEY_DURATION]):
        bind_action(id_, date, done_or_not, scheduled, duration, v, callback, data)


def bind_action(action_id, date, done_or_not: bool, scheduled: bool, duration, v: ViewABC,
                callback: Callable[[dict], None],
                data: dict):
    bind = v.bind_command_to_widget
    bind(f'{c.BTN_DD_DOWN}{action_id}', lambda i=action_id: cmd.upon_increment_button(v, -1, i, data))
    bind(f'{c.BTN_DD_UP}{action_id}', lambda i=action_id: cmd.upon_increment_button(v, 1, i, data))
    bind(f'{c.BTN_REVERT}{action_id}',
         lambda i=action_id: cmd.revert_action(i, date, done_or_not, scheduled, duration, v, data))
    bind(f'{c.BTN_SET_DURATION}{action_id}', lambda i=action_id: cmd.set_duration(i, v, data[c.KEY_CB_DURATION], data))
    bind(f'{c.CB_DONE}{action_id}',
         lambda i=action_id: cmd.update_label(v, i, cmd.decide_text_color(action_id, v), data))
    bind(f'{c.ENTRY_DURATION}{action_id}', lambda *_: cmd.update_widgets_appearances(v, data))
    bind(f'{c.CB_SCHEDULED}{action_id}', lambda *_: cmd.update_widgets_appearances(v, data))
    bind_mouse_hover(action_id, v, data)

    entry_id = f'{c.ACTION_NAME}{action_id}'
    v.bind_left_click(lambda e: print(f'Right clicked {v.get_value(entry_id)}'), entry_id)
    v.bind_right_click(lambda e: cmd.upon_right_click(v, callback, data, action_id), entry_id)
    v.bind_middle_click(lambda e: print(f'Middle clicked {v.get_value(entry_id)}'), entry_id)


def bind_mouse_hover(action_id, v: ViewABC, data: dict):
    aid = action_id

    for key in (
            c.BTN_DD_UP, c.BTN_DD_DOWN, c.ENTRY_DD, c.CB_DONE, c.ACTION_NAME, c.OWNER, c.BTN_REVERT, c.CB_SCHEDULED,
            c.ENTRY_DURATION):
        v.bind_mouse_enter(lambda i=aid: cmd.update_label(v, i, c.SELECTION_COLOR, data), f'{key}{aid}')
        v.bind_mouse_leave(lambda i=aid: cmd.update_label(v, i, cmd.decide_text_color(action_id, v), data),
                           f'{key}{aid}')
