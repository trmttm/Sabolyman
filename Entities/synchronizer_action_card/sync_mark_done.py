from typing import Callable

from Entities.abc_entities import EntitiesABC
from Entities.action import Action
from Entities.card import Card
from .abc import SynchronizerABC


def sync_mark_done(e: EntitiesABC, active_card: Card, get_policy_action: Callable[[str], Action]):
    for action in active_card.all_actions:
        def wrapper_mark_done(action_passed: Action):
            def wrapped():
                mark_done_recursively(action_passed, e, get_policy_action)
                # e.set_active_card(parent_cards[0])  # decide what to select

            return wrapped

        def wrapper_mark_not_done(mark_not_done: Callable):
            def wrapped():
                mark_not_done()
                policy_action = get_policy_action(active_card.id)
                if policy_action is not None:
                    policy_action.mark_not_done_programmatically()

            return wrapped

        action.mark_done = wrapper_mark_done(action)
        action.mark_not_done = wrapper_mark_not_done(action.mark_not_done)


def mark_done_recursively(action_passed: Action, e: EntitiesABC, get_policy_action: Callable):
    action_passed.mark_done_programmatically()
    parents = e.get_cards_that_have_action(action_passed)
    for parent_card in parents:
        if parent_card.is_done:
            policy_action = get_policy_action(parent_card.id)  # This has to happen recursively
            if policy_action is not None:
                mark_done_recursively(policy_action, e, get_policy_action)


def synch_mark_done_passively(e: EntitiesABC, synchronizer: SynchronizerABC):
    active_card = e.active_card
    policy_action = synchronizer.get_policy_action(active_card.id)
    if policy_action is not None:
        if active_card.is_done:
            policy_action.mark_done_programmatically()
            parent_cards = synchronizer.get_immediate_parents(active_card)
            if len(parent_cards) > 0:
                e.set_active_card(parent_cards[0])
        else:
            policy_action.mark_not_done_programmatically()
