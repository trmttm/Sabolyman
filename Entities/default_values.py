import datetime


class DefaultValues:

    @property
    def card_name(self) -> str:
        return f'Default Card Name'

    @property
    def dead_line(self) -> datetime.datetime:
        return datetime.datetime.today()

    @property
    def client_name(self) -> str:
        return 'Client Name'

    @property
    def importance(self) -> int:
        return 5

    @property
    def action_name(self) -> str:
        return f'Default Action Name'

    @property
    def action_time_expected(self) -> datetime.timedelta:
        return datetime.timedelta(0, 60 * 60 * 1)
