from typing import Callable

from Entities.abc_entities import EntitiesABC
from Entities.action import Action
from . import constants
from .abc import SynchronizerABC
from .sync_mark_done import synch_mark_done_passively


def synchronize_remove_action(entities: EntitiesABC, synchronizer: SynchronizerABC):
    entities.unwrapped_remove_action = entities.remove_action
    entities.remove_action = wrapper(entities.unwrapped_remove_action, synchronizer, entities)


def wrapper(remove_action: Callable, synchronizer: SynchronizerABC, e: EntitiesABC):
    def wrapped(action: Action):
        remove_action(action)  # Wrapped / extended method
        action_id = action.id
        if synchronizer.action_has_implementation_card(action_id):
            implementation_card = synchronizer.get_implementation_card(action_id)
            if synchronizer.number_of_immediate_parents(implementation_card) == 0:
                remove_implementation_card(action.id)
        synch_mark_done_passively(e, synchronizer)
        update_card_list()

    def remove_implementation_card(action_id):
        if synchronizer.action_has_implementation_card(action_id):
            implementation_card = synchronizer.get_implementation_card(action_id)
            synchronizer.deregister_by_action(action_id)
            remove_card(implementation_card)

    def remove_card(implementation_card):
        if implementation_card is not None:
            kwargs = {constants.REMOVE_CARD: implementation_card}
            synchronizer.notify(**kwargs)

    def update_card_list():
        kwargs = {constants.UPDATE_CARD_LIST: True}
        synchronizer.notify(**kwargs)

    return wrapped
