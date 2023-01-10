from typing import Callable

from Entities import Action
from Entities import Card


def sync_dead_line(policy_action: Action, get_implementation_card: Callable[[str], Card]):
    def wrapper_set(method: Callable, action: Action):
        def wrapped(*args, **kwargs):
            if not kwargs.get('unwrap'):
                implementation_card = get_implementation_card(action.id)
                action.unwrapped_set_dead_line(implementation_card.dead_line_max())
            return method(*args, **kwargs)

        return wrapped

    def wrapper_get(method: Callable, action: Action):
        def wrapped(*args, **kwargs):
            if not kwargs.get('unwrap'):
                implementation_card = get_implementation_card(action.id)
                current_dead_line = action.unwrapped_get_dead_line()
                new_dead_line = args[0]
                days = (new_dead_line - current_dead_line).days

                implementation_card.increment_deadline_by(days)
            method(*args, **kwargs)

        return wrapped

    policy_action.unwrapped_get_dead_line = policy_action.get_dead_line
    policy_action.unwrapped_set_dead_line = policy_action.set_dead_line
    policy_action.get_dead_line = wrapper_set(policy_action.get_dead_line, policy_action)
    policy_action.set_dead_line = wrapper_get(policy_action.set_dead_line, policy_action)
