import datetime
from typing import Dict
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
from .sorter import Sorter
from .synchronizer_action_card import SynchronizerActionCard


class Entities(EntitiesABC):

    def __init__(self):
        user_name = 'Taro Yamaka'
        self._cards = Cards()
        self._default_values = DefaultValues(user_name)
        self._user = Person(user_name)
        self._show_this_card = None
        self._filter_key = ''
        self._filter_mode = self.all_filter_modes[0]
        self._sorter = Sorter(self._cards)
        self._synchronizer_action_card = SynchronizerActionCard(self)
        self._copied_action = ()

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
    def all_cards(self) -> Tuple[Card, ...]:
        return tuple(self._cards.all_cards)

    @property
    def all_actions(self) -> Tuple[Action, ...]:
        all_actions = []
        for card_ in self.all_cards:
            all_actions += card_.all_actions
        return tuple(all_actions)

    @property
    def my_visible_cards(self) -> Tuple[Card, ...]:
        return self._visible_cards(self.my_cards)

    @property
    def their_visible_cards(self) -> Tuple[Card, ...]:
        return self._visible_cards(self.their_cards)

    @property
    def card_filter_is_on(self) -> bool:
        return self._filter_key not in ['', None]

    def _visible_cards(self, cards_tuple: Tuple[Card, ...]) -> Tuple[Card, ...]:
        visible_cards = cards_tuple

        # Filter 1
        if self._filter_mode == 'Owner' and self._cards.hide_finished_cards:
            visible_cards = tuple(c for c in visible_cards if c.get_search_undone_owner_result(self._filter_key) > 0)
        elif self._filter_mode == 'Owner':
            visible_cards = tuple(c for c in visible_cards if c.get_search_owner_result(self._filter_key) > 0)
        elif self._filter_mode == 'Action Name':
            visible_cards = tuple(c for c in visible_cards if c.get_search_action_name(self._filter_key) > 0)
        elif self._filter_mode == 'Card Name':
            visible_cards = tuple(c for c in visible_cards if c.get_search_card_name(self._filter_key) > 0)
        elif self._filter_mode == 'Client Name':
            visible_cards = tuple(c for c in visible_cards if c.get_search_action_client_name(self._filter_key) > 0)
        else:
            if self.card_filter_is_on:
                visible_cards = tuple(c for c in visible_cards if c.get_search_all_result(self._filter_key) > 0)

        # Filter 2
        if self._cards.hide_finished_cards:
            visible_cards = tuple(c for c in visible_cards if not c.is_done)
        return visible_cards

    def set_filter_key(self, search_key: str, search_mode: str):
        self._filter_key = search_key
        self._filter_mode = search_mode
        for card_ in self._cards.all_cards:
            card_.set_actions_true_colors()

    @property
    def filter_key(self) -> str:
        return self._filter_key

    def clear_filter_key(self):
        self._filter_key = ''
        for card_ in self._cards.all_cards:
            card_.clear_actions_highlight()

    @property
    def all_filter_modes(self) -> Tuple[str, ...]:
        return 'All', 'Owner', 'Action Name', 'Card Name', 'Client Name'

    @property
    def filter_mode(self) -> str:
        return self._filter_mode

    def clear_filter_mode(self):
        self._filter_mode = self.all_filter_modes[0]

    # Getters
    def get_my_card_by_index(self, index: int) -> Card:
        if self._cards.hide_finished_cards or self.card_filter_is_on:
            return get_card_by_index(self.my_visible_cards, index)
        else:
            return get_card_by_index(self.my_cards, index)

    def get_their_card_by_index(self, index: int) -> Card:
        if self._cards.hide_finished_cards or self.card_filter_is_on:
            return get_card_by_index(self.their_visible_cards, index)
        else:
            return get_card_by_index(self.their_cards, index)

    def get_their_visible_card_by_index(self, index: int) -> Card:
        return get_card_by_index(self.their_visible_cards, index)

    def get_my_visible_cards_by_indexes(self, indexes: Tuple[int, ...]) -> Tuple[Card, ...]:
        return tuple(c for (n, c) in enumerate(self.my_visible_cards) if n in indexes)

    def get_their_visible_cards_by_indexes(self, indexes: Tuple[int, ...]) -> Tuple[Card, ...]:
        return tuple(c for (n, c) in enumerate(self.their_visible_cards) if n in indexes)

    def get_action_by_index(self, index: int) -> Action:
        actions_ = self._actions
        if actions_:
            return actions_.get_action_by_index(index)

    def get_action_by_id(self, action_id: str) -> Action:
        return self.get_action_id_to_action().get(action_id)

    def get_card_by_id(self, card_id: str) -> Card:
        return self.get_card_id_to_card().get(card_id)

    def get_card_id_to_card(self) -> Dict[str, Card]:
        card_ids = tuple(c.id for c in self.all_cards if c.id is not None)
        all_cards = tuple(c for c in self.all_cards if c.id is not None)
        return dict(zip(card_ids, all_cards))

    def get_action_id_to_action(self) -> Dict[str, Action]:
        action_ids = tuple(c.id for c in self.all_actions if c.id is not None)
        all_actions = tuple(c for c in self.all_actions if c.id is not None)
        return dict(zip(action_ids, all_actions))

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
        return self.sort_cards(indexes, self.my_visible_cards, shift)

    def move_their_cards(self, indexes: Tuple[int, ...], shift: int):
        return self.sort_cards(indexes, self.their_visible_cards, shift)

    def sort_cards(self, indexes: Tuple[int, ...], cards_: Tuple[Card, ...], shift: int):
        self._sorter.sort_cards_by_manual()
        d, sorted_cards = Utilities.get_tuple_and_destinations_after_shifting_elements(cards_, indexes, shift)
        self._cards.sort_cards(sorted_cards)
        return d

    def sort_cards_by_deadline(self):
        self._sorter.sort_cards_by_deadline()

    def sort_cards_by_name(self):
        self._sorter.sort_cards_by_name()

    def sort_cards_by_current_owner(self):
        self._sorter.sort_cards_by_current_owner()

    def sort_cards_by_current_client(self):
        self._sorter.sort_cards_by_current_client()

    def sort_cards_by_color(self):
        self._sorter.sort_cards_by_color()

    def move_actions_up(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        active_card = self.active_card
        if active_card is not None:
            return self.sort_actions(active_card, indexes, -1)

    def move_actions_down(self, indexes: Tuple[int, ...]) -> Tuple[int, ...]:
        active_card = self.active_card
        if active_card is not None:
            return self.sort_actions(active_card, indexes, 1)

    def sort_actions(self, card: Card, indexes, shift) -> Tuple[int, ...]:
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

    def set_show_this_card(self, card: Card):
        self._show_this_card = card

    def clear_show_this_card(self):
        self._show_this_card = None

    def hide_finished_cards(self):
        self._cards.set_hide_finished_cards(True)

    def unhide_finished_cards(self):
        self._cards.set_hide_finished_cards(False)

    def toggle_hide_finished_cards(self):
        self._cards.toggle_hide_finished_cards()

    def synchronize(self, action_policy: Action, card_implementation: Card):
        sync = self._synchronizer_action_card
        sync.synchronize(action_policy, card_implementation)

    # Properties
    def load_state(self, state: dict):
        self._cards.load_state(state)
        self._synchronizer_action_card.load_state(state)

    @property
    def state(self) -> dict:
        state = self._cards.state
        state.update(self._synchronizer_action_card.state)
        return state

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
                return self.my_visible_cards.index(active_card)
            elif active_card in self.their_cards:
                return self.their_visible_cards.index(active_card)

    @property
    def active_card_is_in_their_cards(self) -> bool:
        return self.active_card in self.their_cards

    @property
    def active_action(self) -> Action:
        if self._actions is not None:
            return self._actions.active_action

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

    @property
    def selected_actions_indexes(self) -> Tuple[int, ...]:
        return self.active_card.selected_actions_indexes

    @property
    def selected_actions(self) -> Tuple[Action, ...]:
        return self.active_card.selected_actions

    def copy_actions(self, actions_passed: Tuple[Action, ...]):
        self._copied_action = actions_passed

    @property
    def copied_actions(self) -> Tuple[Action, ...]:
        return self._copied_action

    @property
    def user(self) -> Person:
        return self._user

    @property
    def sort_by(self) -> str:
        return self._sorter.sort_by

    def sorter_values(self, cards_: Tuple[Card, ...]) -> Tuple[str, ...]:
        return self._sorter.sorter_values(cards_)


def get_card_by_index(cards_tuple, index) -> Card:
    try:
        target_card = cards_tuple[index]
    except IndexError:
        target_card = None
    return target_card
