import datetime
from typing import Callable
from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_card_list


def execute(indexes1: Tuple[int, ...], indexes2: Tuple[int, ...], show_my_card: Callable,
            show_their_card: callable, e: EntitiesABC, p: PresentersABC):
    initial_index = e.active_card_index
    is_my_card = e.active_card_is_in_my_cards

    def upon_user_chooses_date(date: datetime.date):
        if date is not None:
            if is_my_card:
                for n, card in enumerate(e.my_visible_cards):
                    if n in indexes1:
                        card.reset_starting_date_to(date)

                show_my_card((initial_index,))
            else:
                for n, card in enumerate(e.their_visible_cards):
                    if n in indexes2:
                        card.reset_starting_date_to(date)
                show_their_card((initial_index,))

            present_card_list.execute(e, p)

    p.ask_user_date(upon_user_chooses_date)
