from .abc_entity import EntityABC


class File(EntityABC):

    def __init__(self, name: str = ''):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> dict:
        state = {
            'name': self._name
        }
        return state

    def load_state(self, state: dict):
        name = state.get('name', '')
        self._name = name
