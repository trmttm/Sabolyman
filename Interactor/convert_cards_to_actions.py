from typing import Tuple

from Entities import Card
from Entities import EntitiesABC
from Presenters import PresentersABC
from . import add_new_action
from . import add_new_card
from . import get_selected_cards_and_their_indexes
from . import present_card_list


def wrapped_execute(e: EntitiesABC, p: PresentersABC, all_cards: Tuple[Card, ...], indexes: Tuple[int, ...]):
    cards_selected = tuple(card for (n, card) in enumerate(all_cards) if n in indexes)
    card_names = tuple(c.name for c in cards_selected)
    card_deadlines = tuple(c.get_dead_line() for c in cards_selected)

    if cards_selected:
        add_new_card.execute(e, p)
        for name, dead_line in zip(card_names, card_deadlines):
            add_new_action.execute(e, p)
            e.active_action.set_name(name)
            e.active_action.set_dead_line(dead_line)
        present_card_list.execute(e, p)


def execute(e: EntitiesABC, p: PresentersABC, left_indexes_and_right_indexes: Tuple[Tuple[int, ...], ...],
            feedback_method):
    all_cards, indexes = get_selected_cards_and_their_indexes.execute(e, left_indexes_and_right_indexes)

    def action_upon_ok():
        wrapped_execute(e, p, all_cards, indexes)

    title = 'Cards will be deleted'
    body = "The following card(s) will be removed as they are converted to Actions.\nThis cannot be undone.\n\n"
    for (n, card) in enumerate(all_cards):
        if n in indexes:
            body += f'  {n} {card.name}\n'
    feedback_method(title, body, 600, action_ok=lambda *_: action_upon_ok())
