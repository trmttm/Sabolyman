from Entities.abc_entities import EntitiesABC
from Presenters.abc import PresentersABC

from . import show_action_information


def execute(e: EntitiesABC, p: PresentersABC, names: tuple, paths: tuple):
    e.add_action_resources(names, paths)

    kwargs = {}
    """ Tree view options
    strikethroughs = kwargs.get('strikethroughs', tuple(False for _ in names))
    colors = kwargs.get('colors', tuple('Black' for _ in names))
    underlines = kwargs.get('underlines', tuple(False for _ in names))
    bolds = kwargs.get('bolds', tuple(False for _ in names))
    text_colors = kwargs.get('text_colors', tuple('Black' for _ in names))
    """
    show_action_information.execute(e, p, (e.active_action_index,))
