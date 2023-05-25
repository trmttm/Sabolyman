import datetime
from typing import Callable

import GUI.list_of_actions.commands as cmd
import GUI.list_of_actions.gui_components as components
import Utilities
from GUI import ask_user_for_entries
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
    v.bind_command_to_widget(c.BTN_REPLACE, lambda: ask_user_what_to_replace(v, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_REVERT_ALL, lambda: cmd.revert_all(v, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_APPLY, lambda: cmd.apply(v, callback, data))
    v.bind_command_to_widget(c.BTN_ACTIONS_OK, lambda: cmd.upon_ok(v, callback, data))

    cmd.set_initial_label_appearances(v, data)


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
