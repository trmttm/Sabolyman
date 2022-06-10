from Commands import DuplicateCard
from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC

from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, original_card: Card):
    command = DuplicateCard(e, original_card)
    command.execute()
    present_card_list(e, p)
    e.set_show_this_card(e.active_card)
