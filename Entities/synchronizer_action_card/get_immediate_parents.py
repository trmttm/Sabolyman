from Entities.abc_entities import EntitiesABC
from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC


def execute(child_card: Card, e: EntitiesABC, parents: list = None) -> list[Card, ...]:
    s: SynchronizerABC = e.synchronizer
    if parents is None:
        parents = []

    for card in e.all_cards:
        for action in card.all_actions:
            implementation_card = s.get_implementation_card(action.id)
            if implementation_card is not None:
                if implementation_card.id == child_card.id:
                    parents.append(card)
    return parents
