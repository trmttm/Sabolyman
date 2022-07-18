from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, client_name: str):
    action = e.active_action
    if action is not None:
        if client_name == e.user.name:
            person = e.user
        else:
            person = e.create_new_person(client_name)
        action.set_client(person)
