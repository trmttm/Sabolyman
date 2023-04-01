import os

from Entities.abc_entities import EntitiesABC
from Gateway.abc import GatewayABC
from Presenters.abc import PresentersABC
from . import add_new_card
from . import load_template_card


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC):
    def callback(file_name):
        if file_name is None:
            pass
        elif file_name == 'default':
            add_new_card.execute(e, p)
        else:
            load_template_card.execute(e, g, p, os.path.join(g.cards_template_path, file_name))

    file_names = g.get_files_in_the_folder(g.cards_template_path)
    display = ('Default',) + tuple(f.split('.')[0] for f in file_names if f[0] != '.')
    data = ('default',) + tuple(f for f in file_names if f[0] != '.')

    p.ask_user_to_select_from_a_list(dict(zip(display, data)), callback)
