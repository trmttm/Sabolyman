from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, owner_name: str):
    action = e.active_action
    if action is not None:
        if owner_name == e.user.name:
            person = e.user
        else:
            person = e.create_new_person(owner_name)
        action.set_owner(person)

        p.update_action_owner(action.owner.name)
