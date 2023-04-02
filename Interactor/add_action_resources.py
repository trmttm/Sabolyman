from Entities.abc_entities import EntitiesABC
from Presenters.abc import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, paths: tuple):
    e.add_action_resources(paths)

    kwargs = {}
    """ Tree view options
    strikethroughs = kwargs.get('strikethroughs', tuple(False for _ in names))
    colors = kwargs.get('colors', tuple('Black' for _ in names))
    underlines = kwargs.get('underlines', tuple(False for _ in names))
    bolds = kwargs.get('bolds', tuple(False for _ in names))
    text_colors = kwargs.get('text_colors', tuple('Black' for _ in names))
    """

    p.update_action_resources(e.get_action_resources(), **kwargs)
