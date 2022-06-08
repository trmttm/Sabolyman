from typing import Tuple

from Entities import Card
from Entities import EntitiesABC


def execute(e: EntitiesABC, cards: Tuple[Card, ...], indexes: Tuple[int, ...]):
    # Treeview events recursively select and display the card that was not originally displayed (=used by user)
    # e.show_this_card specifies what cards to display.
    card = e.show_this_card
    if card:
        e.set_active_card(card)
    if card in cards:
        indexes = (e.active_card_index,)
        e.clear_show_this_card()
    return indexes
