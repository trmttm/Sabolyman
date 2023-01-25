import datetime

from Entities import EntitiesABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC):
    def upon_date_selected(date: datetime.datetime.date):
        e.set_filter_due_date(date)
        present_card_list.execute(e, p)

    p.ask_user_date(upon_date_selected)
