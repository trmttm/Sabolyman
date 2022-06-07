from Entities import EntitiesABC
from Gateway import GatewayABC


def execute(e: EntitiesABC, g: GatewayABC, file_name: str):
    active_card = e.active_card
    if active_card is not None:
        g.save_file(file_name, active_card.state)
