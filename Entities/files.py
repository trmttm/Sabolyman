from typing import List
from typing import Tuple

from .file import File


class Files:
    def __init__(self):
        self._files: List[File] = []

    def add_file(self, file: File):
        self._files.append(file)

    @property
    def names(self) -> Tuple[str, ...]:
        return tuple(f.name for f in self._files)
