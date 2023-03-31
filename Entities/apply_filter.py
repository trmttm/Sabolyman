from typing import Tuple

from Entities.abc_entities import EntitiesABC
from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC


def execute(cards_tuple: Tuple[Card, ...], e: EntitiesABC):
    visible_cards: Tuple[Card, ...] = cards_tuple

    visible_cards = filter_by_parent_card(e, visible_cards)
    visible_cards = filter_by_due_date(e, visible_cards)
    visible_cards = filter_by_search_key(e, visible_cards)
    visible_cards = filter_by_finished_status(e, visible_cards)
    return visible_cards


def filter_by_parent_card(e: EntitiesABC, visible_cards: Tuple[Card, ...]) -> Tuple[Card, ...]:
    filter_ = e.filter
    s: SynchronizerABC = e.synchronizer
    if filter_.filter_parent_card_id is not None:
        parent_card = e.get_card_by_id(filter_.filter_parent_card_id)
        unordered_visible_cards = set(c for c in s.get_all_descendants(parent_card) if c in visible_cards)
        visible_cards = tuple(c for c in visible_cards if c in unordered_visible_cards)  # maintain card order
    return visible_cards


def filter_by_due_date(e: EntitiesABC, visible_cards: Tuple[Card, ...]) -> Tuple[Card, ...]:
    if e.filter.filter_due_date is not None:
        filter_due_date = e.filter.filter_due_date
        due_today = tuple(c for c in visible_cards if c.dead_line.date() == filter_due_date)
        undone = tuple(c for c in visible_cards if (c.dead_line.date() < filter_due_date and not c.is_done))
        visible_cards = due_today + undone
    return visible_cards


def filter_by_search_key(e: EntitiesABC, visible_cards: Tuple[Card, ...]) -> Tuple[Card, ...]:
    filter_mode = e.filter.filter_mode
    filter_key = e.filter.filter_key

    if filter_mode == 'Owner' and e.filter.hide_finished_cards:
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
        if e.filter.card_filter_is_on:
            visible_cards = tuple(c for c in visible_cards if c.get_search_all_result(filter_key) > 0)

    return visible_cards


def filter_by_finished_status(e: EntitiesABC, visible_cards: Tuple[Card, ...]) -> Tuple[Card, ...]:
    if e.filter.hide_finished_cards:
        visible_cards = tuple(c for c in visible_cards if not c.is_done)
    return visible_cards
