from typing import Callable
from typing import List

from . import constants
from .abc import SynchronizerABC
from ..action import Action
from ..card import Card


def sync_mutually(action_policy: Action, card_implementation: Card, synchronizer: SynchronizerABC):
    syncing_methods = [action_policy.set_name, card_implementation.set_name]
    action_policy.set_name = wrapper_mutual(syncing_methods, synchronizer)
    card_implementation.set_name = wrapper_mutual(syncing_methods, synchronizer)

    syncing_methods = [action_policy.set_color, card_implementation.set_color]
    action_policy.set_color = wrapper_mutual(syncing_methods, synchronizer)
    card_implementation.set_color = wrapper_mutual(syncing_methods, synchronizer)


def wrapper_mutual(methods: List[Callable], s: SynchronizerABC):
    def wrapped_method(*args, **kwargs):
        for f in methods:
            f(*args, **kwargs)
            kw = {constants.UPDATE_CARD_LIST: True}
            s.notify(**kw)

    return wrapped_method
