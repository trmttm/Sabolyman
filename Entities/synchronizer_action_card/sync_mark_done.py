from typing import Callable

from Entities.abc_entities import EntitiesABC
from Entities.action import Action
from Entities.card import Card
from .abc import SynchronizerABC


def sync_mark_done(e: EntitiesABC, implementation_card: Card, get_policy_action: Callable[[str], Action]):
    synchronizer: SynchronizerABC = e.synchronizer
    for action in implementation_card.all_actions:
        def wrapper_mark_done(mark_done: Callable):
            def wrapped():
                mark_done()
                if implementation_card.is_done:
                    policy_action = get_policy_action(implementation_card.id)
                    if policy_action is not None:
                        policy_action.mark_done_programmatically()
                        parent_cards = synchronizer.get_immediate_parents(e.active_card)
                        if len(parent_cards) > 0:
                            e.set_active_card(parent_cards[0])

            return wrapped

        def wrapper_mark_not_done(mark_not_done: Callable):
            def wrapped():
                mark_not_done()
                policy_action = get_policy_action(implementation_card.id)
                if policy_action is not None:
                    policy_action.mark_not_done_programmatically()

            return wrapped

        action.mark_done = wrapper_mark_done(action.mark_done)
        action.mark_not_done = wrapper_mark_not_done(action.mark_not_done)


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
