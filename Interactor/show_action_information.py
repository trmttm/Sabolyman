import datetime
from typing import Tuple

from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    if (len(indexes) > 0) and (None not in indexes):
        index = indexes[0]
        action = e.get_action_by_index(index)
        if action is not None:
            e.set_active_action(action)

            p.update_action_name(action.name)
            p.update_action_date_created(action.date_created)
            p.update_action_time_expected(action.time_expected)
            p.update_action_owner(action.owner.name)
            p.update_action_client(action.client.name)
            p.update_action_is_done(action.is_done)
            p.update_action_description(action.description)
            p.update_action_files(action.files.names)
            p.update_action_due_date(action.dead_line)

        else:
            p.update_action_name('')
            p.update_action_date_created(datetime.datetime.now())
            p.update_action_time_expected(e.default_action_time_expected)
            p.update_action_owner('')
            p.update_action_client(e.default_client_name)
            p.update_action_is_done(False)
            p.update_action_description('')
            p.update_action_files(())
            p.update_action_due_date(e.default_dead_line)
