from Entities.abc_entities import EntitiesABC
from Presenters.abc import PresentersABC

from . import show_action_information


def execute(e: EntitiesABC, p: PresentersABC, paths: tuple):
    def callback(entries: tuple):
        names = entries
        e.add_action_resources(names, paths)
        show_action_information.execute(e, p, (e.active_action_index,))

    kwargs = {
        'title': 'Name Recourses',
        'message': 'Set names for the following resources',
        'default_values': paths,
    }
    p.ask_user_for_entries(callback, **kwargs)
