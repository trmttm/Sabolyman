from typing import Tuple

import Utilities

from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, next_selection_index: Tuple[int, ...] = ()):
    action_names = e.action_names
    f = Utilities.get_two_digit_str_from_int
    s: SynchronizerABC = e.synchronizer
    if action_names is not None:
        second_column_data = tuple(f'{d.year}/{f(d.month)}/{f(d.day)} {f(d.hour)}:{f(d.minute)}'
                                   if d != '' else ''
                                   for d in e.times_completed)
        response_model = action_names, second_column_data, next_selection_index
        states = tuple(a.is_done for a in e.active_card.all_actions)
        back_ground_colors = tuple(a.color for a in e.active_card.all_actions)
        kwargs = {
            'states': states,
            'back_ground_colors': back_ground_colors,
            'text_colors': tuple('blue' if s.action_has_implementation_card(a.id) else 'black'
                                 for a in e.active_card.all_actions),
        }
        p.updates_card_actions(*response_model, **kwargs)
    else:
        print('Select Card first. No Card is selected.')
