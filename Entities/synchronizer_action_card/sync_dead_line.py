from typing import Callable

from Entities.abc_entities import EntitiesABC
from Entities.action import Action
from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC


def sync_dead_line(policy_action: Action, get_implementation_card: Callable[[str], Card], e: EntitiesABC):
    s: SynchronizerABC = e.synchronizer

    def wrapper_get(action: Action):
        def wrapped(*args, **kwargs):
            implementation_card = get_implementation_card(action.id)
            if implementation_card is not None:
                action.set_dead_line_programmatically(implementation_card.dead_line_max())
            return action.get_dead_line_programmatically()

        return wrapped

    def wrapper_set(action: Action):
        def wrapped(*args, **kwargs):
            actions_already_handled = {action.id}
            set_dead_line_recursively(action, get_implementation_card, e, s, args, kwargs, actions_already_handled)

        return wrapped

    if not policy_has_already_been_wrapped(policy_action):
        # wrapping policy action (only, not implementation card)
        policy_action.get_dead_line = wrapper_get(policy_action)
        policy_action.set_dead_line = wrapper_set(policy_action)
        policy_action.has_already_been_wrapped_to_sync_deadline = True
    else:
        # 'second attempt to wrap prevented'
        pass


def policy_has_already_been_wrapped(a: Action):
    try:
        return a.has_already_been_wrapped_to_sync_deadline
    except AttributeError:
        return False


def set_dead_line_recursively(action: Action, get_implementation_card: Callable, e: EntitiesABC,
                              s: SynchronizerABC, args, kwargs, already_handled: set):
    already_handled.add(action.id)
    if action.id not in already_handled:
        implementation_card = get_implementation_card(action.id)
        if implementation_card is not None:
            current_dead_line = action.get_dead_line_programmatically()
            new_dead_line = args[0]
            days = (new_dead_line - current_dead_line).days
            implementation_card.increment_deadline_by(days)
        action.set_dead_line_programmatically(*args, **kwargs)
        cards = e.get_cards_that_have_action(action)
        for card in cards:
            parent_cards = s.get_immediate_parents(card)
            for each_parent_card in parent_cards:
                ancestor_action = s.get_policy_action(each_parent_card.id)
                set_dead_line_recursively(ancestor_action, get_implementation_card, e, s, args, kwargs, already_handled)
