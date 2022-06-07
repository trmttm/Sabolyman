from Entities import EntitiesABC
from Gateway import GatewayABC
from Interactor import present_action_list
from Interactor import present_my_card_list
from Interactor import present_their_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, file_name: str):
    state = g.load_file(file_name)
    e.load_state(state)
    present_my_card_list(e, p, (0,))
    present_their_card_list(e, p, (0,))
    present_action_list(e, p, (0,))
