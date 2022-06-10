from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, client_name: str):
    card = e.active_card
    if card is not None:
        if client_name == e.user.name:
            person = e.user
        else:
            person = e.create_new_person(client_name)
        card.set_client(person)
