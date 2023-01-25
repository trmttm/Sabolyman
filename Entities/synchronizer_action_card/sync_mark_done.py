from typing import Callable

from Entities import Action
from Entities import Card


def sync_mark_done(implementation_card: Card, get_policy_action: Callable):
    for action in implementation_card.all_actions:
        def wrapper_mark_done(a: Action):
            def wrapped():
                a.unwrapped_mark_done()
                if implementation_card.is_done:
                    policy_action = get_policy_action(implementation_card.id)
                    if policy_action is not None:
                        policy_action.mark_done()

            return wrapped

        def wrapper_mark_not_done(a: Action):
            def wrapped():
                a.unwrapped_mark_not_done()
                policy_action = get_policy_action(implementation_card.id)
                if policy_action is not None:
                    policy_action.mark_not_done()

            return wrapped

        action.unwrapped_mark_done = action.mark_done
        action.unwrapped_mark_not_done = action.mark_not_done
        action.mark_done = wrapper_mark_done(action)
        action.mark_not_done = wrapper_mark_not_done(action)
