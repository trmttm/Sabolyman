from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC
from .present_action_list import present_action_list
from .present_card_list import present_card_list


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, file_name: str):
    state = g.load_file(file_name)
    e.load_state(state)
    present_card_list(e, p)
    present_action_list(e, p, (0,))
