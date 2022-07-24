from typing import Tuple


def execute(cards, e, next_selection_indexes) -> Tuple[tuple, dict]:
    cards_names = tuple(c.name for c in cards)
    sort_by = e.sort_by
    sort_by_values = tuple(c.sort_by_value for c in cards)

    args = cards_names, sort_by, sort_by_values, next_selection_indexes
    
    kwargs = {
        'completions_status': tuple(c.is_done for c in cards),
        'colors': tuple(c.color for c in cards),
    }
    return args, kwargs
