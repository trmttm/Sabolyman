from typing import Callable

from Entities import EntitiesABC
from Entities.action import Action
from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, feedback_method: Callable):
    duplicate_actions, n_new_actions = create_alias_of_action_if_not_duplicate(e)
    remove_actions_if_cut_mode(e)
    handle_done_not_done_status_and_select_the_right_card(e)
    present_actions(e, p, n_new_actions)
    feedback_user_if_duplicate(duplicate_actions, feedback_method)


def create_alias_of_action_if_not_duplicate(e: EntitiesABC):
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


def remove_actions_if_cut_mode(e: EntitiesABC):
    if e.is_cut_mode:
        card_to_cut_action_from = e.card_to_cut_action_from
        for action in card_to_cut_action_from.all_actions:
            if action in e.copied_actions:
                card_to_cut_action_from.actions.remove_action(action)
        e.turn_off_cut_mode()


def handle_done_not_done_status_and_select_the_right_card(e: EntitiesABC):
    if card_was_initially_empty(e) and e.active_card.is_done:
        s: SynchronizerABC = e.synchronizer
        if s.card_has_policy_action(e.active_card.id):
            policy_action = s.get_policy_action(e.active_card.id)
            policy_action.mark_done_programmatically()
            find_and_activate_a_card_that_has_the_policy_action(e, policy_action)


def card_was_initially_empty(e):
    return len(e.active_card.all_actions) == len(e.copied_actions)


def find_and_activate_a_card_that_has_the_policy_action(e, policy_action):
    next_cards_to_select = get_all_visible_cards_that_have_the_policy_action(e, policy_action)
    if len(next_cards_to_select) > 0:
        e.set_active_card(next_cards_to_select[0])
        e.set_show_this_card(e.active_card)
    else:
        pass


def get_all_visible_cards_that_have_the_policy_action(e: EntitiesABC, policy_action: Action) -> tuple[Card, ...]:
    return tuple(c for c in e.all_cards if c.has_action(policy_action) and e.card_is_visible(c))


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
