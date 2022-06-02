from .file import File


class Files:
    def __init__(self):
        self._files = []

    def add_file(self, file: File):
        self._files.append(file)
