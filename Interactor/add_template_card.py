from Commands import AddCard
from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC
from . import present_card_list


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, file_name: str):
    card_state = g.load_file(file_name)
    command = AddCard(e)
    command.execute()
    active_card = e.active_card
    active_card.load_state(card_state)
    active_card.update_date_created()
    active_card.reset_starting_date_to_today()
    present_card_list.execute(e, p)
