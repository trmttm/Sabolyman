from typing import List
from typing import Tuple

from .abc_entity import EntityABC
from .file import File


class Files(EntityABC):
    def __init__(self):
        self._files: List[File] = []
        self._active_file = None

    def add_file(self, file: File):
        self._files.append(file)

    @property
    def names(self) -> Tuple[str, ...]:
        return tuple(f.name for f in self._files)

    def load_state(self, state: dict):
        self.__init__()
        active_file_index = state.get('active_file', 0)
        files_state = state.get('files', {})
        for n, file_state in enumerate(files_state):
            file = File('')
            file.load_state(file_state)
            if n == active_file_index:
                self._active_file = file
