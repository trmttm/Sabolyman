import datetime


def datetime_to_str(d: datetime.datetime):
    due_date_str = f'{d.year}/{d.month}/{d.day} {d.hour}:{d.minute}'
    return due_date_str


def time_delta_to_str(t: datetime.timedelta):
    return str(t)
