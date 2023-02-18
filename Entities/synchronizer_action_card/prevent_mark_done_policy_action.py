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

    if not policy_has_already_been_wrapped(policy_action):
        policy_action.unwrapped_mark_done = policy_action.mark_done
        policy_action.unwrapped_mark_not_done = policy_action.mark_not_done

        policy_action.mark_done = wrapper_mark_done(policy_action.mark_done)
        policy_action.mark_not_done = wrapper_mark_not_done(policy_action.mark_not_done)

        policy_action.has_already_been_wrapped_to_prevent_make_done = True
    else:
        pass


def policy_has_already_been_wrapped(a: Action):
    try:
        return a.has_already_been_wrapped_to_prevent_make_done
    except AttributeError:
        return False
