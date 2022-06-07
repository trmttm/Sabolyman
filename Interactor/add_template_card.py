from Commands import AddCard
from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC
from .present_my_card_list import present_my_card_list
from .present_their_card_list import present_their_card_list


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, file_name: str):
    card_state = g.load_file(file_name)
    command = AddCard(e)
    command.execute()
    active_card = e.active_card
    active_card.load_state(card_state)

    if active_card in e.my_cards:
        present_my_card_list(e, p, (len(e.my_cards) - 1,))
    elif active_card in e.their_cards:
        present_their_card_list(e, p, (len(e.their_cards) - 1,))
