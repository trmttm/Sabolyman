from typing import Callable

from Entities import Action
from Entities import Card


def sync_dead_line(policy_action: Action, get_implementation_card: Callable[[str], Card]):
    def wrapper_get(method: Callable, action: Action):
        def wrapped(*args, **kwargs):
            implementation_card = get_implementation_card(action.id)
            if implementation_card is not None:
                action.unwrapped_set_dead_line(implementation_card.dead_line_max())  # *1
            return method(*args, **kwargs)

        return wrapped

    def wrapper_set(method: Callable, action: Action):
        def wrapped(*args, **kwargs):
            implementation_card = get_implementation_card(action.id)
            if implementation_card is not None:
                current_dead_line = action.unwrapped_get_dead_line()  # *2
                new_dead_line = args[0]
                days = (new_dead_line - current_dead_line).days
                implementation_card.increment_deadline_by(days)
            method(*args, **kwargs)

        return wrapped

    if not policy_has_already_been_wrapped(policy_action):
        # keep unwrapped getter & setter accessible
        policy_action.unwrapped_get_dead_line = policy_action.get_dead_line  # *2
        policy_action.unwrapped_set_dead_line = policy_action.set_dead_line  # *1

        # wrapping policy action (only, not implementation card)
        policy_action.get_dead_line = wrapper_get(policy_action.get_dead_line, policy_action)
        policy_action.set_dead_line = wrapper_set(policy_action.set_dead_line, policy_action)
        policy_action.has_already_been_wrapped = True
    else:
        print('second attempt to wrap')


def policy_has_already_been_wrapped(a: Action):
    try:
        return a.has_already_been_wrapped
    except AttributeError:
        return False
