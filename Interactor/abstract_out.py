from typing import Callable
from typing import Tuple

from Commands import CreateAction
from Entities import EntitiesABC


def execute(e: EntitiesABC, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...], feedback: Callable = None):
    cards_selected = ()
    if e.active_card in e.my_cards:
        cards_selected = e.get_my_visible_cards_by_indexes(indexes1)
    elif e.active_card in e.their_cards:
        cards_selected = e.get_their_visible_cards_by_indexes(indexes2)

    actions_to_copy = []
    for implementation_card in cards_selected:
        command = CreateAction(e)
        policy_action = command.execute()
        e.synchronize_action_to_card(policy_action, implementation_card)
        actions_to_copy.append(policy_action)
    e.copy_actions(tuple(actions_to_copy))

    message = f'Implementation card(s) {actions_to_copy} are copied.'
    if feedback is not None:
        feedback('Abstracted out', f'Implementation card(s) {actions_to_copy} are copied.', 600)
    else:
        print(message)
