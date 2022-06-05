from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, owner_name: str):
    action = e.active_action
    if action is not None:
        person = e.create_new_person(owner_name)
        e.active_action.set_owner(person)

        p.update_action_owner(action.owner.name)
