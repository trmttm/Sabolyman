from Entities import EntitiesABC
from Presenters import PresentersABC
from . import jump_to_card


def execute(e: EntitiesABC, p: PresentersABC):
    card = e.active_card
    policy_action = e.get_policy_action(card.id)
    cards = e.get_cards_that_have_action(policy_action)
    if len(cards) > 0:
        card_containing_policy_action = cards[0]
        indexes_ = (card_containing_policy_action.all_actions.index(policy_action),)
        card_containing_policy_action.select_actions(indexes_)
        jump_to_card.execute(card_containing_policy_action, e, p)
