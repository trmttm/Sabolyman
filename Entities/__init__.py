import datetime
from typing import List
from typing import Tuple

import Utilities

from .abc_entities import EntitiesABC
from .action import Action
from .actions import Actions
from .card import Card
from .cards import Cards
from .default_values import DefaultValues
from .file import File
from .files import Files
from .person import Person


class Entities(EntitiesABC):

    def __init__(self):
        self._cards = Cards()
        self._default_values = DefaultValues()
        self._user = Person('Taro Yamaka')

    # Default Values
    @property
    def default_card_name(self) -> str:
        return self._default_values.card_name

    @property
    def default_dead_line(self) -> datetime.datetime:
        return self._default_values.dead_line

    @property
    def default_importance(self) -> int:
        return self._default_values.importance

    @property
    def default_action_name(self) -> str:
        return self._default_values.action_name

    @property
    def default_action_time_expected(self) -> datetime.timedelta:
        return self._default_values.action_time_expected

    @property
    def my_cards(self) -> Tuple[Card, ...]:
        return tuple(c for c in self._cards.all_cards if c.owner.name == self._user.name)

    @property
    def their_cards(self) -> Tuple[Card, ...]:
        return tuple(c for c in self._cards.all_cards if c.owner.name != self._user.name)

    # Getters
    def get_my_card_by_index(self, index: int) -> Card:
        try:
            return self.my_cards[index]
        except IndexError:
            pass

    def get_their_card_by_index(self, index: int) -> Card:
        try:
            return self.their_cards[index]
        except IndexError:
            pass

    def get_action_by_index(self, index: int) -> Action:
        return self._actions.get_action_by_index(index)

    # Setters
    def set_active_card(self, card: Card):
        self._cards.set_active_card(card)

    def set_active_action(self, action: Action):
        self._actions.set_active_action(action)

    # Factories
    def create_new_person(self, name: str) -> Person:
        return Person(name)

    # User Actions
    def add_new_card(self, card: Card):
        return self._cards.add_new_card(card)

    def remove_card(self, card: Card):
        self._cards.remove_card(card)

    def move_my_cards_up(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        return self.move_my_cards(indexes, -1)

    def move_my_cards_down(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        return self.move_my_cards(indexes, 1)

    def move_their_cards_up(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        return self.move_their_cards(indexes, -1)

    def move_their_cards_down(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        return self.move_their_cards(indexes, 1)

    def move_my_cards(self, indexes: Tuple[int, ...], shift: int):
        return self.sort_cards(indexes, self.my_cards, shift)

    def move_their_cards(self, indexes: Tuple[int, ...], shift: int):
        return self.sort_cards(indexes, self.their_cards, shift)

    def sort_cards(self, indexes, my_cards, shift):
        d, sorted_my_cards = Utilities.get_tuple_and_destinations_after_shifting_elements(my_cards, indexes, shift)
        self._cards.sort_cards(sorted_my_cards)
        return d

    def move_actions_up(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        active_card = self.active_card
        if active_card is not None:
            return self.sort_actions(active_card, indexes, -1)

    def move_actions_down(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        active_card = self.active_card
        if active_card is not None:
            return self.sort_actions(active_card, indexes, 1)

    def sort_actions(self, card, indexes, shift) -> Tuple[int, ...]:
        actions = card.actions.all_actions
        d, sorted_actions = Utilities.get_tuple_and_destinations_after_shifting_elements(actions, indexes, shift)
        self._actions.sort_actions(sorted_actions)
        return d

    def add_new_action(self, action: Action):
        card = self._cards.active_card
        if card is not None:
            card.add_action(action)

    def remove_action(self, action: Action):
        self._actions.remove_action(action)

    # Properties
    def load_state(self, state: dict):
        self._cards.load_state(state)

    @property
    def state(self) -> dict:
        return self._cards.state

    @property
    def all_actions(self) -> List[Action]:
        card = self.active_card
        if card is not None:
            return card.actions.all_actions
        else:
            return []

    @property
    def action_names(self) -> Tuple[str, ...]:
        actions = self._actions
        if actions is not None:
            return actions.action_names

    @property
    def times_expected(self) -> Tuple[datetime.timedelta, ...]:
        return self._actions.times_expected

    @property
    def _actions(self) -> Actions:
        card = self.active_card
        if card is not None:
            return card.actions

    @property
    def active_card(self) -> Card:
        return self._cards.active_card

    @property
    def active_action(self) -> Action:
        return self._actions.active_action

    @property
    def due_dates(self) -> Tuple[datetime.datetime, ...]:
        return self._cards.due_dates

    @property
    def card_names(self) -> Tuple[str, ...]:
        return self._cards.card_names

    @property
    def existing_my_card_due_dates(self) -> Tuple[datetime.datetime, ...]:
        return datetime.datetime(2022, 6, 2), datetime.datetime(2022, 5, 31)

    @property
    def existing_my_card_names(self) -> Tuple[str, ...]:
        return 'Card1', 'Card2',

    @property
    def user(self) -> Person:
        return self._user
