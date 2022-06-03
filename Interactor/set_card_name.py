from interface_view import ViewABC

from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, v: ViewABC):
    card_name = v.get_value('entry_name')
    card = e.active_card
    card.set_name(card_name)
    present_card_list(e, p)
