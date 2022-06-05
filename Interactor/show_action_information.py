from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    if len(indexes) > 0:
        index = indexes[0]
        action = e.get_action_by_index(index)
        if action is not None:
            e.set_active_action(action)
            action_names = e.action_names
            times_expected = e.times_expected

            p.update_action_name(action.name)
            p.update_action_date_created(action.date_created)
            p.update_action_time_expected(action.time_expected)
            p.update_action_owner(action.owner.name)
            p.update_action_is_done(action.is_done)
            p.update_action_description(action.description)
            p.update_action_files(action.files.names)

            # p.updates_action_actions(action_names, expected_times)
