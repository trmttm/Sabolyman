import datetime

from Entities import EntitiesABC


def execute(e: EntitiesABC, done_or_not):
    action = e.active_action
    if done_or_not:
        action.set_completed_time(datetime.datetime.now())
    else:
        action.set_incomplete()
