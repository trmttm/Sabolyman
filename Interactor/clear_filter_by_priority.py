from Entities import EntitiesABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC):
    e.filter.clear_filter_by_priority()
    present_card_list.execute(e, p)
