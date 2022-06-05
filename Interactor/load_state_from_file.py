from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, gateway: GatewayABC, file_name: str):
    state = gateway.load_file(file_name)
    e.load_state(state)
    p.load_state(state)
