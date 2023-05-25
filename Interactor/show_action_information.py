import datetime
from typing import Tuple

from Entities import EntitiesABC
from Entities.action import Action
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, indexes: Tuple[int]):
    if (len(indexes) > 0) and (None not in indexes):
        index = indexes[0]
        action = e.get_action_by_index(index)
        show_action_information_by_action(action, e, p)


def show_action_information_by_action(action: Action, e: EntitiesABC, p: PresentersABC):
    if action is not None:
        e.set_active_action(action)

        p.update_action_name(action.name)
        p.update_action_date_created(action.date_created)
        p.update_action_time_expected(action.time_expected)
        p.update_action_owner(action.get_owner().name)
        p.update_action_client(action.client.name)
        p.update_action_is_done(action.is_done)
        p.update_action_is_scheduled(action.is_scheduled)
        p.update_action_description(action.description)
        p.update_action_files(action.files.names)
        p.update_action_due_date(action.get_dead_line())
        p.update_action_start_from(action.get_start_from())
        p.update_action_resources(action.get_action_resource_names())

    else:
        p.update_action_name('')
        p.update_action_date_created(datetime.datetime.now())
        p.update_action_time_expected(e.default_action_time_expected)
        p.update_action_owner('')
        p.update_action_client(e.default_client_name)
        p.update_action_is_done(False)
        p.update_action_is_scheduled(False)
        p.update_action_description('')
        p.update_action_files(())
        p.update_action_due_date(e.default_dead_line)
        p.update_action_start_from(e.default_start_from)
        p.update_action_resources(e.default_action_resources)
