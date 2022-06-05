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

    @property
    def all_files(self) -> List[File]:
        return self._files

    @property
    def active_file(self) -> File:
        return self._active_file

    @property
    def state(self) -> dict:
        files_state = tuple(f.state for f in self.all_files)
        active_file_index = 0
        for n, file in enumerate(self.all_files):
            if file == self.active_file:
                active_file_index = n

        state = {
            'active_file': active_file_index,
            'files': files_state,
        }
        return state

    def load_state(self, state: dict):
        self.__init__()
        active_file_index = state.get('active_file', 0)
        files_state = state.get('files', {})
        for n, file_state in enumerate(files_state):
            file = File()
            file.load_state(file_state)
            if n == active_file_index:
                self._active_file = file
