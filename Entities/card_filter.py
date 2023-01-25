import datetime
from typing import Union
from typing import Union


class CardFilter:
    def __init__(self):
        self._all_filter_modes = 'All', 'Owner', 'Action Name', 'Card Name', 'Client Name'
        self._filter_mode = self._all_filter_modes[0]
        self._filter_key = ''
        self._filter_due_date = None

    @property
    def all_filter_modes(self) -> tuple:
        return self._all_filter_modes

    @property
    def card_filter_is_on(self) -> bool:
        return self._filter_key not in ['', None]

    @property
    def filter_due_date(self) -> Union[None, datetime.date]:
        return self._filter_due_date

    @property
    def filter_mode(self) -> str:
        return self._filter_mode

    @property
    def filter_key(self) -> str:
        return self._filter_key

    def set_filter_key(self, filter_key: str):
        self._filter_key = filter_key

    def set_filter_mode(self, filter_mode: str):
        self._filter_mode = filter_mode

    def set_filter_due_date(self, filter_due_date: Union[None, datetime.date]):
        self._filter_due_date = filter_due_date

    def clear_filter_mode(self):
        self.set_filter_mode(self._all_filter_modes[0])
