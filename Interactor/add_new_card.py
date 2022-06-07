from Commands import AddCard
from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_my_card_list import present_my_card_list


def execute(e: EntitiesABC, p: PresentersABC):
    command = AddCard(e)
    command.execute()
    next_selection_indexes = (len(e.my_cards) - 1,)

    present_my_card_list(e, p, next_selection_indexes)
