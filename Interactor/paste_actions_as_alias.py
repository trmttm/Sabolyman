from typing import Callable

from Entities import EntitiesABC
from Entities.action import Action
from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Presenters import PresentersABC
from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, feedback_method: Callable):
    feedback, n_new_actions = create_alias_of_action_if_not_duplicate_or_incursion(e)
    handle_done_not_done_status_and_select_the_right_card(e)
    remove_actions_if_cut_mode(e)
    present_actions(e, p, n_new_actions)
    feedback_user_if_duplicate_or_incursion(feedback, feedback_method)


def create_alias_of_action_if_not_duplicate_or_incursion(e: EntitiesABC):
    duplicate_actions = []
    copying_to_itself = []
    feedback = {'duplicate_actions': duplicate_actions, 'copying_to_itself': copying_to_itself, }
    n_new_actions = 0

    for action in e.copied_actions:
        if action in e.active_card.all_actions:
            duplicate_actions.append(action)
        elif check_if_pasting_to_itself(action, e):
            copying_to_itself.append(action)
        else:
            action.set_id()
            e.add_new_action(action)
            n_new_actions += 1
    return feedback, n_new_actions


def check_if_pasting_to_itself(action: Action, e: EntitiesABC) -> bool:
    implementation_card = e.synchronizer.get_implementation_card(action.id)
    if implementation_card is not None:
        return implementation_card.id == e.active_card.id
    else:
        return False


def remove_actions_if_cut_mode(e: EntitiesABC):
    if e.is_cut_mode:
        card_to_cut_action_from = e.card_to_cut_action_from
        for action in tuple(card_to_cut_action_from.all_actions):
            if action in e.copied_actions:
                card_to_cut_action_from.actions.remove_action(action)
        e.turn_off_cut_mode()


def handle_done_not_done_status_and_select_the_right_card(e: EntitiesABC):
    if card_was_initially_empty(e) and e.active_card.is_done:
        s: SynchronizerABC = e.synchronizer
        if s.card_has_policy_action(e.active_card.id):
            policy_action = s.get_policy_action(e.active_card.id)
            policy_action.mark_done_programmatically()
            policy_action.set_completed_time(max(a.time_completed for a in e.active_card.all_actions))
        e.set_active_card(e.card_to_cut_action_from)
        e.set_show_this_card(e.active_card)


def card_was_initially_empty(e):
    return len(e.active_card.all_actions) == len(e.copied_actions)


def get_all_visible_cards_that_have_the_policy_action(e: EntitiesABC, policy_action: Action) -> tuple[Card, ...]:
    return tuple(c for c in e.all_cards if c.has_action(policy_action) and e.card_is_visible(c))


def present_actions(e: EntitiesABC, p: PresentersABC, last_n_actions: int):
    if last_n_actions and e.active_card is not None:
        n_all_actions = len(e.active_card.all_actions)
        next_selection_index = tuple(n_all_actions - last_n_actions + i for i in range(last_n_actions))
        present_action_list.execute(e, p, next_selection_index)


def feedback_user_if_duplicate_or_incursion(feedback, feedback_method):
    actions_that_already_exist_in_active_card = feedback.get('duplicate_actions', [])
    body_text = 'The following alias(es) not created as the actions already exist.'
    feedback_user(actions_that_already_exist_in_active_card, body_text, feedback_method)

    actions_that_is_copying_to_itself = feedback.get('copying_to_itself', [])
    body_text = 'The following alias(es) is tyring to paste to itself.'
    feedback_user(actions_that_is_copying_to_itself, body_text, feedback_method)


def feedback_user(actions_that_already_exist_in_active_card, body_text, feedback_method):
    if actions_that_already_exist_in_active_card:
        title = 'Actions already exist'
        body = '%s\n' % body_text
        for n, action in enumerate(actions_that_already_exist_in_active_card):
            body += f'  {n + 1} {action.name}\n'
        feedback_method(title, body, 600, 200)
