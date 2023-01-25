import datetime
from typing import Union


class CardFilter:
    def __init__(self):
        self._all_filter_modes = 'All', 'Owner', 'Action Name', 'Card Name', 'Client Name'
        self._filter_mode = self._all_filter_modes[0]
        self._filter_key = ''
        self._filter_due_date = None
        self._hide_finished_cards = True

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

    def set_hide_finished_cards(self, true_false: bool):
        self._hide_finished_cards = true_false

    def toggle_hide_finished_cards(self):
        self._hide_finished_cards = not self._hide_finished_cards

    @property
    def hide_finished_cards(self) -> bool:
        return self._hide_finished_cards

    @property
    def state(self) -> dict:
        return {'card_filter_state': {
            'filter_mode': self._filter_mode,
            'filter_key': self._filter_key,
            'filter_due_date': self._filter_due_date,
            'hide_finished_cards': self._hide_finished_cards,
        }}

    def load_state(self, state: dict):
        filter_state = state.get('card_filter_state', {})
        self._filter_mode = filter_state.get('filter_mode', self._all_filter_modes[0])
        self._filter_key = filter_state.get('filter_key', '')
        self._filter_due_date = filter_state.get('filter_due_date', None)
        self._hide_finished_cards = filter_state.get('hide_finished_cards', True)
