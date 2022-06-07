import datetime


def datetime_to_str(d: datetime.datetime):
    f = int_to_str
    due_date_str = f'{d.year}/{f(d.month)}/{f(d.day)} {f(d.hour)}:{f(d.minute)}'
    return due_date_str


def time_delta_to_str(t: datetime.timedelta):
    return str(t)


def int_to_str(i: int) -> str:
    return f'0{i}' if i < 10 else f'{i}'
