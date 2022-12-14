import datetime
from typing import Callable

from Entities import Action
from Entities import EntitiesABC
from . import display_filtered_actions


def execute(from_: str, to_: str, feedback: Callable, e: EntitiesABC):
    title = f'Tasks due between {from_} to {to_}...'
    date_from = datetime.datetime.strptime(from_, '%Y/%m/%d').date()
    date_to = datetime.datetime.strptime(to_, '%Y/%m/%d').date()

    def filter_action(action: Action):
        datetime_in_question = action.dead_line
        if (datetime_in_question is not None) and (not action.is_done):
            date = datetime_in_question.date()
            if (date_from <= date) and (date <= date_to):
                return True
        return False

    display_filtered_actions.execute(title, filter_action, feedback, e)
