from Entities.abc_entities import EntitiesABC
from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC


def execute(child_card: Card, e: EntitiesABC) -> list[Card, ...]:
    s: SynchronizerABC = e.synchronizer
    parents = []

    policy_action = s.get_policy_action(child_card.id)
    if policy_action is not None:
        for card in e.all_cards:
            if policy_action in card.all_actions:
                parents.append(card)
    return parents
