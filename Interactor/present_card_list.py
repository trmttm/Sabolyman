from Entities import EntitiesABC
from Presenters import PresentersABC


def present_card_list(e: EntitiesABC, p: PresentersABC, next_selection_index=None):
    card_names = e.card_names
    due_dates = e.due_dates
    response_model = card_names, due_dates, next_selection_index
    p.update_cards(*response_model)
