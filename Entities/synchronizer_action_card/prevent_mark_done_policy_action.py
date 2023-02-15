from typing import Callable

from Entities import Action
from .abc import SynchronizerABC


def prevent_mark_done_policy_action(policy_action: Action, synchronizer: SynchronizerABC):
    def wrapper_mark_done(mark_done: Callable):
        def wrapped():
            pass  # don't mark done

        return wrapped

    def wrapper_mark_not_done(mark_not_done: Callable):
        def wrapped():
            pass  # don't mark not done

        return wrapped

    policy_action.mark_done = wrapper_mark_done(policy_action.mark_done)
    policy_action.mark_not_done = wrapper_mark_not_done(policy_action.mark_not_done)
