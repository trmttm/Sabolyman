from Entities.abc_entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Gateway import GatewayABC


def execute(e: EntitiesABC, g: GatewayABC, file_name: str):
    active_card = e.active_card
    if active_card is not None:
        s: SynchronizerABC = e.synchronizer
        descendants = s.get_all_descendants(active_card)
        if descendants == [active_card]:
            data = active_card.state
        else:
            data = {
                'is_complex': True,
                'cards_state': tuple(c.state for c in descendants),
                'sync_state': s.state,
            }
        g.save_file(file_name, data)
