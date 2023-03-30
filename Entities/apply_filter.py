from typing import Tuple

from Entities.abc_entities import EntitiesABC
from Entities.card import Card


def execute(cards_tuple: Tuple[Card, ...], e: EntitiesABC):
    s = e.synchronizer
    f = e.filter
    visible_cards = cards_tuple

    # Filter by parent card
    if f.filter_parent_card_id is not None:
        parent_card = e.get_card_by_id(f.filter_parent_card_id)
        visible_cards = tuple(c for c in s.get_all_descendants(parent_card) if c in visible_cards)

    # Filter 0 Filter by due date
    if f.filter_due_date is not None:
        filter_due_date = f.filter_due_date
        due_today = tuple(c for c in visible_cards if c.dead_line.date() == filter_due_date)
        undone = tuple(c for c in visible_cards if (c.dead_line.date() < filter_due_date and not c.is_done))
        visible_cards = due_today + undone

    # Filter 1
    filter_mode = f.filter_mode
    filter_key = f.filter_key
    if filter_mode == 'Owner' and f.hide_finished_cards:
        visible_cards = tuple(c for c in visible_cards if c.get_search_undone_owner_result(filter_key) > 0)
    elif filter_mode == 'Owner':
        visible_cards = tuple(c for c in visible_cards if c.get_search_owner_result(filter_key) > 0)
    elif filter_mode == 'Action Name':
        visible_cards = tuple(c for c in visible_cards if c.get_search_action_name(filter_key) > 0)
    elif filter_mode == 'Card Name':
        visible_cards = tuple(c for c in visible_cards if c.get_search_card_name(filter_key) > 0)
    elif filter_mode == 'Client Name':
        visible_cards = tuple(c for c in visible_cards if c.get_search_action_client_name(filter_key) > 0)
    else:
        if f.card_filter_is_on:
            visible_cards = tuple(c for c in visible_cards if c.get_search_all_result(filter_key) > 0)

    # Filter 2
    if f.hide_finished_cards:
        visible_cards = tuple(c for c in visible_cards if not c.is_done)
    return visible_cards
