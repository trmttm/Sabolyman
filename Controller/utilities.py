from Controller.menu_bar import now
from Entities import EntitiesABC


def default_file_name(e: EntitiesABC) -> str:
    return f'{now()}_{e.user.name.replace(" ", "_")}.sb'