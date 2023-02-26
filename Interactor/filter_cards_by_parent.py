from Entities import EntitiesABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC):
    e.set_filter_parent_card_id(e.active_card.id)
    present_card_list.execute(e, p)
