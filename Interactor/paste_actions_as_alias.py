from typing import Callable

from Entities import EntitiesABC
from Interactor import present_action_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, feedback_method: Callable):
    duplicate_actions, n_new_actions = create_alias_of_action_if_not_duplicate(e)
    present_actions(e, p, n_new_actions)
    feedback_user_if_duplicate(duplicate_actions, feedback_method)


def create_alias_of_action_if_not_duplicate(e):
    duplicate_actions = []
    n_new_actions = 0

    for action in e.copied_actions:
        if action not in e.active_card.all_actions:
            action.set_id()
            e.add_new_action(action)
            n_new_actions += 1
        else:
            duplicate_actions.append(action)
    return duplicate_actions, n_new_actions


def present_actions(e: EntitiesABC, p: PresentersABC, last_n_actions: int):
    if last_n_actions:
        n_all_actions = len(e.active_card.all_actions)
        next_selection_index = tuple(n_all_actions - last_n_actions + i for i in range(last_n_actions))
        present_action_list.execute(e, p, next_selection_index)


def feedback_user_if_duplicate(actions_that_already_exist_in_active_card, feedback_method):
    if actions_that_already_exist_in_active_card:
        title = 'Actions already exist'
        body = 'The following alias(es) not created as the actions already exist.\n'
        for n, action in enumerate(actions_that_already_exist_in_active_card):
            body += f'  {n + 1} {action.name}\n'
        feedback_method(title, body, 600, 200)
