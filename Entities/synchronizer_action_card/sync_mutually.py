from typing import Callable
from typing import List

from ..action import Action
from ..card import Card


def sync_mutually(action_policy: Action, card_implementation: Card):
    syncing_methods = [action_policy.set_name, card_implementation.set_name]
    action_policy.set_name = wrapper_mutual(syncing_methods)
    card_implementation.set_name = wrapper_mutual(syncing_methods)

    syncing_methods = [action_policy.set_color, card_implementation.set_color]
    action_policy.set_color = wrapper_mutual(syncing_methods)
    card_implementation.set_color = wrapper_mutual(syncing_methods)


def wrapper_mutual(methods: List[Callable]):
    def wrapped_method(*args, **kwargs):
        for f in methods:
            f(*args, **kwargs)

    return wrapped_method