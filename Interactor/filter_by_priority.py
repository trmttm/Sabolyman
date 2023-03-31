from Entities import EntitiesABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, priority: int):
    e.filter.set_filter_priority(priority)
    present_card_list.execute(e, p)
