from Entities import EntitiesABC
from Gateway import GatewayABC
from .present_action_list import present_action_list
from .present_my_card_list import present_my_card_list
from .present_their_card_list import present_their_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, file_name: str):
    state = g.load_file(file_name)
    e.load_state(state)
    present_my_card_list(e, p, (0,))
    present_their_card_list(e, p, (0,))
    present_action_list(e, p, (0,))
