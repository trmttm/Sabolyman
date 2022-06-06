from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def present_action_list(e: EntitiesABC, p: PresentersABC, next_selection_index: Tuple[int, ...] = ()):
    action_names = e.action_names
    if action_names is not None:
        times_expected = e.times_expected
        response_model = action_names, times_expected, next_selection_index
        states = tuple(a.is_done for a in e.all_actions)
        p.updates_card_actions(*response_model, states=states)
    else:
        print('Select Card first. No Card is selected.')
