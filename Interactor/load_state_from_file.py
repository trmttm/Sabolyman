from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC
from . import present_action_list
from . import present_card_list


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, file_name: str):
    state = g.load_file(file_name)
    e.load_state(state)
    present_card_list.execute(e, p)
    present_action_list.execute(e, p, (0,))
