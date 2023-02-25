from typing import Callable
from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(datetime_str: str, update_method: Callable, ask_user: Callable, e: EntitiesABC,
            p: PresentersABC, indexes: Tuple[int, ...]):
    action = e.active_action
    if action is not None:
        actions = tuple(e.get_action_by_index(i) for i in indexes)

        if len(actions) > 1:
            message = f'Set {datetime_str} to all of below actions?\n'
            for n, action in enumerate(actions):
                message += f'\n{n}{"" * (5 - len(str(n)))}: {action.name}'

            def action_ok(response: bool):
                if response:
                    update_method(datetime_str, actions, e, p)

            if ask_user is not None:
                ask_user(message, action_ok=action_ok)
        else:
            update_method(datetime_str, actions, e, p)
