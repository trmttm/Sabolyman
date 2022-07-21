import os

from Controller.menu_bar import now
from Entities import EntitiesABC
from Interactor import InteractorABC


def default_file_path(i: InteractorABC, e: EntitiesABC) -> str:
    return os.path.join(i.home_folder, i.state_folder, f'{now()}_{e.user.name.replace(" ", "_")}.sb')


def default_file_name(e: EntitiesABC) -> str:
    return f'{now()}_{e.user.name.replace(" ", "_")}.sb'
