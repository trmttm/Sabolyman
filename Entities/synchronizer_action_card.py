from typing import Callable
from typing import Dict
from typing import List

from .abc_entity import EntityABC
from .action import Action
from .card import Card
from .cards import Cards


class SynchronizerActionCard(EntityABC):
    def __init__(self, cards: Cards):
        self._cards = cards
        self._synchronization_table: Dict[str, str] = {}

        # action.attach_to_state_change(self)

    def synchronize(self, action_policy: Action, card_implementation: Card):
        # TODO implement below
        action_policy.set_id()
        card_implementation.set_id()
        self._synchronization_table[action_policy.id] = card_implementation.id

        # initial synchronization
        card_implementation.set_name(action_policy.name)
        card_implementation.set_color(action_policy.color)

        # wrapping methods
        syncing_methods = [action_policy.set_name, card_implementation.set_name]
        action_policy.set_name = wrapper_mutual(syncing_methods)

        # Name

        '''
                What happens when
                1) action_policy state is changed?
                    deadline is extended
                    deadline is shortened -> balls at their court must be modified.
                2) card_implementation state is changed?
                3) action_policy is deleted
                    all of the lower_level actions at their court must be notified to cancel.
                4) card_implementation is deleted
                    high level policy action can also be deleted?

                ...fix the semantics first.
        '''
        pass

    def load_state(self, state: dict):
        pass

    @property
    def state(self) -> dict:
        return {}


def wrapper_mutual(methods: List[Callable]):
    def wrapped_method(*args, **kwargs):
        for f in methods:
            f(*args, **kwargs)

    return wrapped_method
