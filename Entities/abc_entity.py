import abc


class EntityABC(abc.ABC):
    @abc.abstractmethod
    def load_state(self, state: dict):
        pass

    @property
    @abc.abstractmethod
    def state(self) -> dict:
        pass
