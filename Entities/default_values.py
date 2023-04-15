import datetime


class DefaultValues:
    def __init__(self, user_name: str = None):
        self._user_name = user_name or 'Client Name'

    @property
    def card_name(self) -> str:
        return f'New Goal'

    @property
    def dead_line(self) -> datetime.datetime:
        tm = datetime.datetime.today() + datetime.timedelta(0)
        return datetime.datetime(tm.year, tm.month, tm.day, 17, 0)

    @property
    def start_from(self) -> datetime.datetime:
        tm = datetime.datetime.today() + datetime.timedelta(0)
        return datetime.datetime(tm.year, tm.month, tm.day, 17, 0)

    @property
    def default_action_resources(self) -> tuple:
        return ()

    @property
    def client_name(self) -> str:
        return self._user_name

    @property
    def importance(self) -> int:
        return 5

    @property
    def action_name(self) -> str:
        return f'Identify next action'

    @property
    def action_time_expected(self) -> datetime.timedelta:
        return datetime.timedelta(0, 60 * 60 * 0)
