import datetime


class DefaultValues:

    @property
    def card_name(self) -> str:
        return f'新たなカード'

    @property
    def dead_line(self) -> datetime.datetime:
        return datetime.datetime.today()

    @property
    def importance(self) -> int:
        return 5

    @property
    def action_name(self) -> str:
        return f'新たなアクション'

    @property
    def action_time_expected(self) -> datetime.timedelta:
        return datetime.timedelta(1)
