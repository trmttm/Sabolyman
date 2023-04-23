import datetime
from typing import Callable

from Entities import Action
from Entities import EntitiesABC
from Entities.synchronizer_action_card import SynchronizerABC
from . import display_filtered_actions

text_color = 'dark green'


def execute(from_: str, to_: str, feedback: Callable, e: EntitiesABC):
    title = f'Progress from {from_} to {to_}...'
    date_from = datetime.datetime.strptime(from_, '%Y/%m/%d').date()
    date_to = datetime.datetime.strptime(to_, '%Y/%m/%d').date()
    s: SynchronizerABC = e.synchronizer

    def filter_action(action: Action):
        datetime_in_question = action.time_completed
        if (datetime_in_question is not None) and (not s.action_has_implementation_card(action.id)):
            date = datetime_in_question.date()
            if (date_from <= date) and (date <= date_to):
                return True
        return False

    display_filtered_actions.execute(title, filter_action, feedback, e, text_color=text_color)
