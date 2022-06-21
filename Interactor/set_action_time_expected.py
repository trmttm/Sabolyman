import datetime

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, time_expected_str: str):
    action = e.active_action
    if action is not None:
        time_expected = time_delta_str_to_time_delta(time_expected_str)
        action.set_time_expected(time_expected)
        present_action_list.execute(e, p, (e.active_action_index,))


def time_delta_str_to_time_delta(time_expected_str) -> datetime.timedelta:
    if 'day' in time_expected_str:
        try:
            str_before_days, str_rest = time_expected_str.split('day,')
        except ValueError:
            str_before_days, str_rest = time_expected_str.split('days,')
    else:
        str_before_days = '0'
        str_rest = time_expected_str
    days = int(str_before_days)
    hours_str, minutes_str, seconds_str = str_rest.split(':')
    hours, minutes, seconds = int(hours_str), int(minutes_str), int(seconds_str)
    total_seconds = 60 * 60 * hours + 60 * minutes + seconds

    return datetime.timedelta(days, total_seconds)
