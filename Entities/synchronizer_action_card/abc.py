import abc
from typing import Union

from Entities import Card


class SynchronizerABC(abc.ABC):
    @abc.abstractmethod
    def get_implementation_card(self, action_id: str) -> Union[Card, None]:
        pass

    @abc.abstractmethod
    def deregister_by_action(self, action_id):
        pass

    @abc.abstractmethod
    def action_has_implementation_card(self, action_id: str) -> bool:
        pass
