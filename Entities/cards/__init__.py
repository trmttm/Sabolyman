from typing import List
from typing import Tuple

from Entities.card import Card

from . import state_io
from .abc import CardsABC


class Cards(CardsABC):

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

    def sort_cards(self, sorted_cards: Tuple[Card, ...]):
        new_cards_list = [c for c in self._cards if c not in sorted_cards]
        new_cards_list += list(sorted_cards)
        self._cards = new_cards_list

    @property
    def card_names(self) -> Tuple[str, ...]:
        return tuple(c.name for c in self._cards)

    @property
    def all_cards(self) -> List[Card]:
        return self._cards

    def remove_card(self, card: Card):
        self._cards.remove(card)

    def get_card_by_id(self, card_id: str) -> Card:
        for card in self._cards:
            if card.id == str:
                return card

    @property
    def state(self) -> dict:
        return state_io.create_state(self)

    def load_state(self, state: dict):
        state_io.load_state(self, state)
