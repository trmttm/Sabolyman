from Entities import EntitiesABC
from Presenters import PresentersABC


def present_action_list(e: EntitiesABC, p: PresentersABC, next_selection_index=None):
    action_names = e.action_names
    times_expected = e.times_expected
    response_model = action_names, times_expected, next_selection_index
    p.updates_card_actions(*response_model)
