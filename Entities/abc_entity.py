import abc


class EntityABC(abc.ABC):
    def load_state(self, state: dict):
        pass
