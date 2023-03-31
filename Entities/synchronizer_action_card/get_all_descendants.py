from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC


def execute(parent_card: Card, s: SynchronizerABC, descendants: list = None) -> list[Card, ...]:
    if descendants is None:
        descendants = []
    if parent_card is not None:
        descendants.append(parent_card)
        for a in parent_card.all_actions:
            if s.action_has_implementation_card(a.id):
                implementation_card = s.get_implementation_card(a.id)
                execute(implementation_card, s, descendants)
    return descendants
