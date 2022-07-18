from typing import Callable
from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, dead_line_str: str, trees_selected_indexes: Tuple[Tuple[int, ...], ...],
            ask_user: Callable):
    card = e.active_card
    if card is not None:
        if e.active_card_is_in_my_cards:
            indexes = trees_selected_indexes[0]
            cards = tuple(e.get_my_card_by_index(i) for i in indexes)
        else:
            indexes = trees_selected_indexes[1]
            cards = tuple(e.get_their_card_by_index(i) for i in indexes)

        if len(cards) > 1:
            message = f'Set dead line = {dead_line_str} to all of below cards?\n'
            for n, card in enumerate(cards):
                message += f'\n{n}{"" * (5 - len(str(n)))}: {card.name}'

            def ok_action(response: bool):
                if response:
                    update_cards_dead_lines(dead_line_str, cards, e, p)

            ask_user(message, action_ok=ok_action)
        else:
            update_cards_dead_lines(dead_line_str, cards, e, p)


def update_cards_dead_lines(dead_line_str: str, cards: tuple, e: EntitiesABC, p: PresentersABC):
    for card in cards:
        card.set_dead_line_by_str(dead_line_str)
        present_card_list.execute(e, p)
