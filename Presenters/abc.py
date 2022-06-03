import abc
import datetime
from typing import Tuple


class PresentersABC(abc.ABC):

    @abc.abstractmethod
    def update_cards(self, names: Tuple[str, ...], due_dates: Tuple[datetime.datetime, ...], select_nth: int = None):
        pass

    @abc.abstractmethod
    def update_card_name(self, name: str):
        pass

    @abc.abstractmethod
    def update_card_date_created(self, date_created: datetime.datetime):
        pass

    @abc.abstractmethod
    def update_card_due_date(self, due_date: datetime.datetime):
        pass

    @abc.abstractmethod
    def updates_card_actions(self):
        pass
