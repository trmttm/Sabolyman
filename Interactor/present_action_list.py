from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, next_selection_index: Tuple[int, ...] = ()):
    action_names = e.action_names
    if action_names is not None:
        # second_column_data = e.times_expected
        second_column_data = e.times_completed
        response_model = action_names, second_column_data, next_selection_index
        states = tuple(a.is_done for a in e.all_actions)
        p.updates_card_actions(*response_model, states=states)
    else:
        print('Select Card first. No Card is selected.')
