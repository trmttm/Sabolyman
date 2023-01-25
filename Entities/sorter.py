from typing import Tuple

import Utilities

from .card import Card
from .cards import CardsABC

MANUAL = 'Manual'
DEAD_LINE = 'Due Date'
NAME = 'Name'
CURRENT_OWNER = 'Current Owner'
CURRENT_CLIENT = 'Current Client'
COLOR = 'Color'


class Sorter:
    def __init__(self, cards: CardsABC):
        self._cards = cards
        self._sort_by = MANUAL

    def set_sort_by(self, sort_by: str):
        self._sort_by = sort_by

    @property
    def sort_by(self) -> str:
        return self._sort_by

    def sorter_values(self, cards_: Tuple[Card, ...]) -> Tuple[str, ...]:
        if self._sort_by == DEAD_LINE:
            return tuple(Utilities.datetime_to_str(c.dead_line) for c in cards_)
        elif self._sort_by in (NAME, COLOR):
            return tuple('' for _ in cards_)
        elif self._sort_by == CURRENT_OWNER:
            return tuple(c.current_owner.name for c in cards_)
        elif self._sort_by == CURRENT_CLIENT:
            return tuple(c.current_client.name for c in cards_)
        else:
            return tuple(Utilities.datetime_to_str(c.dead_line) for c in cards_)

    def sort_cards_by_manual(self):
        self.set_sort_by(MANUAL)

    def sort_cards_by_deadline(self):
        list_sorter = [c.dead_line for c in self._cards.all_cards]
        self._sort(DEAD_LINE, list_sorter)

    def sort_cards_by_name(self):
        list_sorter = [c.name for c in self._cards.all_cards]
        self._sort(NAME, list_sorter)

    def sort_cards_by_current_owner(self):
        list_sorter = [c.current_owner.name for c in self._cards.all_cards]
        self._sort(CURRENT_OWNER, list_sorter)

    def sort_cards_by_current_client(self):
        list_sorter = [c.current_client.name for c in self._cards.all_cards]
        self._sort(CURRENT_CLIENT, list_sorter)

    def sort_cards_by_color(self):
        list_sorter = [c.color for c in self._cards.all_cards]
        self._sort(COLOR, list_sorter)

    def _sort(self, mode: str, list_sorter: list):
        self.set_sort_by(mode)
        _, sorted_cards = Utilities.sort_lists(list_sorter, self._cards.all_cards)
        self._cards.sort_cards(tuple(sorted_cards))

    @property
    def state(self) -> dict:
        return {'sorter_state': {
            'sort_by': self._sort_by
        }}

    def load_state(self, state: dict):
        sorter_state = state.get('sorter_state', {})
        self._sort_by = sorter_state.get('sort_by', MANUAL)
