from interface_view import ViewABC

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import add_new_card
from . import delete_selected_cards
from . import set_card_name
from . import set_dead_line
from . import show_card_information
from .abc import InteractorABC


class Interactor(InteractorABC):
    def __init__(self, entities: EntitiesABC, presenters: PresentersABC, view: ViewABC):
        self._args = entities, presenters, view

    def add_new_card(self):
        add_new_card.execute(*self._args)

    def delete_selected_cards(self):
        delete_selected_cards.execute(*self._args)

    def show_card_information(self):
        show_card_information.execute(*self._args)

    def set_card_name(self):
        set_card_name.execute(*self._args)

    def set_dead_line(self):
        set_dead_line.execute(*self._args)
