from interface_view import ViewABC

from Entities import EntitiesABC
from Presenters import PresentersABC
from .present_card_list import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, v: ViewABC):
    dead_line_str = v.get_value('entry_dead_line')
    card = e.active_card
    card.set_dead_line_by_str(dead_line_str)
    present_card_list(e, p)
