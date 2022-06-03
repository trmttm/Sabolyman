from interface_view import ViewABC

from Commands import AddCard
from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, *_: ViewABC):
    command = AddCard(e)
    command.execute()
    next_selection_index = len(e.all_cards) - 1

    present_card_list(e, p, next_selection_index)
