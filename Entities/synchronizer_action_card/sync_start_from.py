from typing import Callable

from Entities.action import Action
from Entities.card import Card


def sync_start_from(policy_action: Action, get_implementation_card: Callable[[str], Card]):
    def wrapper_get(method: Callable, action: Action):
        def wrapped(*args, **kwargs):
            implementation_card = get_implementation_card(action.id)
            if implementation_card is not None:
                action.unwrapped_set_start_from(implementation_card.start_from_min())  # *1
            return method(*args, **kwargs)

        return wrapped

    def wrapper_set(method: Callable, action: Action):
        def wrapped(*args, **kwargs):
            implementation_card = get_implementation_card(action.id)
            if implementation_card is not None:
                current_start_from = action.unwrapped_get_start_from()  # *2
                new_start_from = args[0]
                days = (new_start_from - current_start_from).days
                implementation_card.increment_start_from_by(days)
            method(*args, **kwargs)

        return wrapped

    if not policy_has_already_been_wrapped(policy_action):
        # keep unwrapped getter & setter accessible
        policy_action.unwrapped_get_start_from = policy_action.get_start_from  # *2
        policy_action.unwrapped_set_start_from = policy_action.set_start_from  # *1

        # wrapping policy action (only, not implementation card)
        policy_action.get_start_from = wrapper_get(policy_action.get_start_from, policy_action)
        policy_action.set_start_from = wrapper_set(policy_action.set_start_from, policy_action)
        policy_action.has_already_been_wrapped_to_sync_start_from = True
    else:
        # 'second attempt to wrap prevented'
        pass


def policy_has_already_been_wrapped(a: Action):
    try:
        return a.has_already_been_wrapped_to_sync_start_from
    except AttributeError:
        return False
