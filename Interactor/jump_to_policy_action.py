from typing import Callable

from Entities.abc_entities import EntitiesABC
from Entities.card import Card
from Presenters import PresentersABC

from . import jump_to_card


def execute(e: EntitiesABC, p: PresentersABC, callback_select_tree: Callable):
    card = e.active_card
    policy_action = e.get_policy_action(card.id)
    cards = e.get_cards_that_have_action(policy_action)
    if len(cards) == 1:
        jump_to_one_and_the_only_one_card(callback_select_tree, cards, e, p, policy_action)
    elif len(cards) > 1:
        ask_user_and_decide_where_to_jump_to(callback_select_tree, cards, e, p, policy_action)
    else:  # len(cards) == 0
        no_jump(callback_select_tree, e)


def jump_to_one_and_the_only_one_card(callback_select_tree, cards, e, p, policy_action):
    card_containing_policy_action = cards[0]
    action_index = jump(card_containing_policy_action, policy_action, e, p)
    callback_select_tree(e.active_card_is_in_my_cards, e.active_card_index, action_index)


def ask_user_and_decide_where_to_jump_to(callback_select_tree, cards, e, p, policy_action):
    def callback_jump(card_id: str):
        for candidate in cards:
            if candidate.id == card_id:
                card_selected_by_user = candidate
                action_index_ = jump(card_selected_by_user, policy_action, e, p)
                callback_select_tree(e.active_card_is_in_my_cards, e.active_card_index, action_index_)

    p.ask_user_to_select_from_a_list(dict(zip(tuple(c.name for c in cards), tuple(c.id for c in cards))), callback_jump)


def no_jump(callback_select_tree, e):
    callback_select_tree(e.active_card_is_in_my_cards, e.active_card_index, e.active_action_index)


def jump(card_containing_policy_action: Card, policy_action, e: EntitiesABC, p: PresentersABC):
    indexes_ = (card_containing_policy_action.all_actions.index(policy_action),)
    card_containing_policy_action.select_actions(indexes_)
    jump_to_card.execute(card_containing_policy_action, e, p)
    action_index = e.get_action_index(card_containing_policy_action, policy_action)
    return action_index
