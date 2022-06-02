from Entities import Card
from Entities import File
from .abc import UseCase


class AddFileToCard(UseCase):
    def __init__(self, card: Card, file: File):
        self._card = card
        self._file = file

    def execute(self):
        self._card.add_file(self._file)
