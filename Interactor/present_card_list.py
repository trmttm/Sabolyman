from Entities import EntitiesABC
from Presenters import PresentersABC


def present_card_list(e: EntitiesABC, p: PresentersABC, next_selection_index=None):
    my_cards = tuple(c for c in e.all_cards if c.owner.name == e.user.name)
    my_cards_names = tuple(c.name for c in e.all_cards if c.owner.name == e.user.name)
    my_cards_due_dates = tuple(c.due_date for c in e.all_cards if c.owner.name == e.user.name)

    their_cards_names = tuple(c.name for c in e.all_cards if c not in my_cards)
    their_cards_due_dates = tuple(c.due_date for c in e.all_cards if c not in my_cards)

    response_model = my_cards_names, my_cards_due_dates, next_selection_index
    p.update_my_cards(*response_model)

    response_model = their_cards_names, their_cards_due_dates, next_selection_index
    p.update_their_cards(*response_model)
