from typing import Callable
from typing import Tuple

from Entities import Action
from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list
from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, dead_line_str: str, indexes: Tuple[int, ...],
            ask_user: Callable = None):
    action = e.active_action
    if action is not None:
        actions = tuple(e.get_action_by_index(i) for i in indexes)

        if len(actions) > 1:
            message = f'Set dead line = {dead_line_str} to all of below actions?\n'
            for n, action in enumerate(actions):
                message += f'\n{n}{"" * (5 - len(str(n)))}: {action.name}'

            def action_ok(response: bool):
                if response:
                    update_actions_dead_lines(dead_line_str, actions, e, p)

            if ask_user is not None:
                ask_user(message, action_ok=action_ok)
        else:
            update_actions_dead_lines(dead_line_str, actions, e, p)


def update_actions_dead_lines(dead_line_str: str, actions: Tuple[Action, ...], e: EntitiesABC, p: PresentersABC):
    for action in actions:
        action.set_dead_line_by_str(dead_line_str)
        present_card_list.execute(e, p)
        present_action_list.execute(e, p)
