from Entities.abc_entities import EntitiesABC
from Entities.action import Action
from Entities.synchronizer_action_card.abc import SynchronizerABC


def sync_dead_line(policy_action: Action, e: EntitiesABC):
    s: SynchronizerABC = e.synchronizer

    def wrapper_get(action: Action):
        def wrapped(*args, **kwargs):
            implementation_card = s.get_implementation_card(action.id)
            if implementation_card is not None:
                action.set_dead_line_programmatically(implementation_card.dead_line_max())
            return action.get_dead_line_programmatically()

        return wrapped

    def wrapper_set(action: Action):
        def wrapped(*args, **kwargs):
            actions_already_handled = set()
            set_dead_line_recursively(action, e, args, kwargs, actions_already_handled)

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


def set_dead_line_recursively(action: Action, e: EntitiesABC, args, kwargs, already_handled: set):
    if (action is not None) and action.id not in already_handled:
        already_handled.add(action.id)
        synch_with_implementation_card(action, args, e)
        action.set_dead_line_programmatically(*args, **kwargs)
        synch_with_higher_level_recursively(action, already_handled, args, e, kwargs)


def synch_with_implementation_card(action: Action, args, e: EntitiesABC):
    s: SynchronizerABC = e.synchronizer
    implementation_card = s.get_implementation_card(action.id)
    if implementation_card is not None:
        current_dead_line = action.get_dead_line_programmatically()
        new_dead_line = args[0]
        days = (new_dead_line - current_dead_line).days
        implementation_card.increment_deadline_by(days)


def synch_with_higher_level_recursively(action: Action, already_handled: set, args, e: EntitiesABC, kwargs):
    cards = e.get_cards_that_have_action(action)
    s: SynchronizerABC = e.synchronizer
    for card in cards:
        parent_cards = s.get_immediate_parents(card)
        for each_parent_card in parent_cards:
            ancestor_action = s.get_policy_action(each_parent_card.id)
            set_dead_line_recursively(ancestor_action, e, args, kwargs, already_handled)
