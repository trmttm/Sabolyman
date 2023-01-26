from Entities import Action
from Entities import EntitiesABC
from . import constants
from .abc import SynchronizerABC
from .sync_dead_line import sync_dead_line
from .sync_mark_done import sync_mark_done
from .sync_mutually import sync_mutually


def synchronize_add_new_action(entities: EntitiesABC, s: SynchronizerABC):
    def wrapper_add_new_action(e: EntitiesABC):
        def wrapped(a: Action):
            implementation_card = e.active_card
            policy_action: Action = s.get_policy_action(implementation_card.id)

            e.unwrapped_add_new_action(a)

            sync_mutually(a, implementation_card)
            sync_dead_line(a, s.get_implementation_card)
            sync_mark_done(implementation_card, s.get_policy_action)

            if policy_action is not None:
                policy_action.mark_not_done()
            kwargs = {constants.UPDATE_CARD_LIST: True}
            s.notify(**kwargs)

        return wrapped

    entities.unwrapped_add_new_action = entities.add_new_action
    entities.add_new_action = wrapper_add_new_action(entities)
