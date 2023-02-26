from typing import Tuple
from typing import Union

from Entities import Card
from Entities import EntitiesABC


def execute(e: EntitiesABC, target_cards: Tuple[Card, ...], indexes: Tuple[int, ...]) -> Union[Tuple[int, ...], None]:
    # Treeview events recursively select and display the card that was not originally displayed (=used by user)
    # e.show_this_card specifies what cards to display.
    card_to_show_specified = e.show_this_card
    if card_to_show_specified and e.card_is_visible(card_to_show_specified):
        e.set_active_card(card_to_show_specified)
        if card_to_show_specified in target_cards:  # cards_ vs their_cards
            modified_indexes = (e.active_card_index,)
            e.clear_show_this_card()
            return modified_indexes
        else:
            return None
    else:
        return indexes
