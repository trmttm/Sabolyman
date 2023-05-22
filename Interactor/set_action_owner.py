from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC

from . import present_card_list


def execute(e: EntitiesABC, p: PresentersABC, owner_name: str, actions_indexes: Tuple[int, ...]):
    for i, action in enumerate(e.active_card.all_actions):
        if i in actions_indexes:
            if owner_name == e.user.name:
                person = e.user
            else:
                person = e.create_new_person(owner_name)
            action.set_owner(person)

            p.update_action_owner(action.get_owner().name)
            present_card_list.execute(e, p)
