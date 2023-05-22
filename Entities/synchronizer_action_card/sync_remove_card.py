from typing import Callable

from Entities.abc_entities import EntitiesABC
from Entities.card import Card

from . import constants
from .abc import SynchronizerABC


def synchronize_remove_card(entities: EntitiesABC, synchronizer: SynchronizerABC):
    entities.unwrapped_remove_card = entities.remove_card
    entities.remove_card = wrapper(entities.unwrapped_remove_card, synchronizer, entities)


def wrapper(remove_card: Callable, synchronizer: SynchronizerABC, e: EntitiesABC):
    def wrapped(card: Card):
        remove_card(card)  # Wrapped / extended method
        card_to_select = decide_what_card_to_select_next(card)
        remove_policy_action(card.id)
        remove_actions_implementation_cards(card, e.synchronizer)
        select_next_card_correctly(card_to_select)
        update_card_list()

    def decide_what_card_to_select_next(card: Card):
        card_to_select = None
        if synchronizer.card_has_policy_action(card.id):
            policy_action = synchronizer.get_policy_action(card.id)
            for c in e.all_cards:
                if c.has_action(policy_action):
                    card_to_select = c
        else:
            if len(e.my_cards) > 0:
                card_to_select = e.my_cards[0]
            elif len(e.their_visible_cards) > 0:
                card_to_select = e.their_cards[0]
        return card_to_select

    def remove_policy_action(card_id):
        if synchronizer.card_has_policy_action(card_id):
            policy_action = synchronizer.get_policy_action(card_id)
            synchronizer.deregister_by_card(card_id)
            remove_action(policy_action)

    def remove_actions_implementation_cards(card: Card, s: SynchronizerABC):
        # Recursively remove implementation cards
        for action in card.all_actions:
            implementation_card = synchronizer.get_implementation_card(action.id)
            if (implementation_card is not None) and s.number_of_immediate_parents(implementation_card) == 0:
                wrapped(implementation_card)

    def select_next_card_correctly(card: Card):
        if card is not None:
            e.set_active_card(card)

    def remove_action(policy_action):
        if policy_action is not None:
            kwargs = {constants.REMOVE_ACTION: policy_action}
            synchronizer.notify(**kwargs)

    def update_card_list():
        kwargs = {constants.UPDATE_CARD_LIST: True}
        synchronizer.notify(**kwargs)

    return wrapped
