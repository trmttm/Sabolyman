from Entities.abc_entities import EntitiesABC
from Entities.action import Action
from . import constants
from .abc import SynchronizerABC
from .sync_mark_done import sync_mark_done


def synchronize_add_new_action(entities: EntitiesABC, s: SynchronizerABC):
    def wrapper_add_new_action(e: EntitiesABC):
        def wrapped(new_action: Action):
            active_card = e.active_card
            policy_action: Action = s.get_policy_action(active_card.id)

            e.unwrapped_add_new_action(new_action)
            sync_mark_done(entities, active_card, s.get_policy_action)

            if policy_action is not None:
                policy_action.mark_not_done()
            kwargs = {constants.UPDATE_CARD_LIST: True}
            s.notify(**kwargs)

        return wrapped

    entities.unwrapped_add_new_action = entities.add_new_action
    entities.add_new_action = wrapper_add_new_action(entities)
