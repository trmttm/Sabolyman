import datetime
from typing import List
from typing import Tuple

from .abc import EntitiesABC
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

    # Getters
    def get_card_by_index(self, index: int) -> Card:
        return self._cards.get_card_by_index(index)

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

    def add_new_action(self, action: Action):
        card = self._cards.active_card
        if card is not None:
            card.add_action(action)

    # Properties
    @property
    def all_actions(self) -> List[Action]:
        card = self.active_card
        if card is not None:
            return card.actions.all_actions
        else:
            return []

    @property
    def action_names(self) -> Tuple[str, ...]:
        return self._actions.action_names

    @property
    def times_expected(self) -> Tuple[datetime.timedelta, ...]:
        return self._actions.times_expected

    @property
    def _actions(self) -> Actions:
        return self.active_card.actions

    @property
    def active_card(self) -> Card:
        return self._cards.active_card

    @property
    def active_action(self) -> Action:
        return self._actions.active_action

    @property
    def all_cards(self) -> List[Card]:
        return self._cards.all_cards

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
        return Person('山家太郎')
