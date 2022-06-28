import datetime
from typing import List
from typing import Tuple
from typing import Union

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
        self._show_this_card = None

    # Default Values
    @property
    def default_card_name(self) -> str:
        return self._default_values.card_name

    @property
    def default_dead_line(self) -> datetime.datetime:
        return self._default_values.dead_line

    @property
    def default_client_name(self) -> str:
        return self._default_values.client_name

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

    @property
    def my_visible_cards(self) -> Tuple[Card, ...]:
        return self._visible_cards(self.my_cards)

    @property
    def their_visible_cards(self) -> Tuple[Card, ...]:
        return self._visible_cards(self.their_cards)

    def _visible_cards(self, cards_tuple: Tuple[Card, ...]) -> Tuple[Card, ...]:
        if self._cards.hide_finished_cards:
            visible_cards = tuple(c for c in cards_tuple if not c.is_done)
        else:
            visible_cards = cards_tuple
        return visible_cards

    # Getters
    def get_my_card_by_index(self, index: int) -> Card:
        if self._cards.hide_finished_cards:
            return get_card_by_index(self.my_visible_cards, index)
        else:
            return get_card_by_index(self.my_cards, index)

    def get_their_card_by_index(self, index: int) -> Card:
        if self._cards.hide_finished_cards:
            return get_card_by_index(self.their_visible_cards, index)
        else:
            return get_card_by_index(self.their_cards, index)

    def get_their_visible_card_by_index(self, index: int) -> Card:
        return get_card_by_index(self.their_visible_cards, index)

    def get_my_cards_by_indexes(self, indexes: Tuple[int, ...]) -> Tuple[Card, ...]:
        return tuple(c for (n, c) in enumerate(self.my_cards) if n in indexes)

    def get_their_cards_by_indexes(self, indexes: Tuple[int, ...]) -> Tuple[Card, ...]:
        return tuple(c for (n, c) in enumerate(self.their_cards) if n in indexes)

    def get_action_by_index(self, index: int) -> Action:
        actions = self._actions
        if actions:
            return actions.get_action_by_index(index)

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
    def times_completed(self) -> Tuple[datetime.datetime, ...]:
        return self._actions.times_completed

    @property
    def _actions(self) -> Actions:
        card = self.active_card
        if card is not None:
            return card.actions

    @property
    def active_card(self) -> Card:
        return self._cards.active_card

    @property
    def active_card_is_in_my_cards(self) -> bool:
        return self.active_card in self.my_cards

    @property
    def active_card_index(self) -> int:
        if self._cards is not None:
            active_card = self.active_card
            if active_card in self.my_cards:
                return self.my_cards.index(active_card)
            elif active_card in self.their_cards:
                return self.their_cards.index(active_card)

    @property
    def active_card_is_in_their_cards(self) -> bool:
        return self.active_card in self.their_cards

    @property
    def active_action(self) -> Action:
        if self._actions is not None:
            return self._actions.active_action

    def set_show_this_card(self, card: Card):
        self._show_this_card = card

    def clear_show_this_card(self):
        self._show_this_card = None

    @property
    def show_this_card(self) -> Union[None, Card]:
        return self._show_this_card

    @property
    def active_action_index(self) -> int:
        if self._actions is not None:
            active_action = self.active_action
            if active_action is not None:
                index = self._actions.all_actions.index(active_action)
                return None if index is None else index

    def hide_finished_cards(self):
        self._cards.set_hide_finished_cards(True)

    def unhide_finished_cards(self):
        self._cards.set_hide_finished_cards(False)

    @property
    def user(self) -> Person:
        return self._user


def get_card_by_index(cards_tuple, index) -> Card:
    try:
        target_card = cards_tuple[index]
    except IndexError:
        target_card = None
    return target_card
