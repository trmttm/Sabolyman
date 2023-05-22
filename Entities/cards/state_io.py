from Entities import Card

from .abc import CardsABC


def create_state(cards: CardsABC) -> dict:
    card_states = tuple(c.state for c in cards.all_cards)
    active_card_index = 0
    for n, card in enumerate(cards.all_cards):
        if card == cards.active_card:
            active_card_index = n
    state = {
        'cards': {
            'card': card_states,
        },
        'active_card': active_card_index,
    }
    return state


def load_state(cards: CardsABC, state: dict):
    cards.__init__()
    cards_state = state.get('cards', {})
    card_states = cards_state.get('card', ())
    active_card_index = cards_state.get('active_card', 0)

    alias_action_dictionary = {}
    for n, card_state in enumerate(card_states):
        card = Card()
        card.load_state(card_state, alias_action_dictionary)
        cards.add_new_card(card)
        if n == active_card_index:
            cards.set_active_card(card)
