import datetime
from typing import List
from typing import Tuple

from .abc_entity import EntityABC
from .card import Card


class Cards(EntityABC):
    def __init__(self):
        self._cards: List[Card, ...] = []
        self._active_card = None

    @property
    def active_card(self) -> Card:
        return self._active_card

    def set_active_card(self, card: Card):
        self._active_card = card

    def add_new_card(self, card: Card):
        self._cards.append(card)

    def get_card_by_index(self, index: int) -> Card:
        try:
            return self._cards[index]
        except IndexError:
            pass

    @property
    def card_names(self) -> Tuple[str, ...]:
        return tuple(c.name for c in self._cards)

    @property
    def due_dates(self) -> Tuple[datetime.datetime, ...]:
        return tuple(c.due_date for c in self._cards)

    @property
    def all_cards(self) -> List[Card]:
        return self._cards

    def remove_card(self, card: Card):
        self._cards.remove(card)

    def load_state(self, state: dict):
        self.__init__()

        cards_state = state.get('cards', {})
        card_states = cards_state.get('card', ())
        active_card_index = cards_state.get('active_card', 0)
        for n, card_state in enumerate(card_states):
            card = Card()
            card.load_state(card_state)

            self.add_new_card(card)
            if n == active_card_index:
                self.set_active_card(card)
