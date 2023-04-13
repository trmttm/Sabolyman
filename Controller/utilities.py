import os

from Controller.menu_bar import now
from Entities import EntitiesABC
from Interactor import InteractorABC


def default_file_path(i: InteractorABC, e: EntitiesABC) -> str:
    return os.path.join(i.home_folder, i.state_folder, f'{now()}_{e.user.name.replace(" ", "_")}.sb')


def default_file_name(e: EntitiesABC) -> str:
    return f'{now()}_{e.user.name.replace(" ", "_")}.sb'


def get_paths(e):
    separator = '__||__'
    if ' /' in e.data or ' ¥' in e.data:
        # 正しい可能性を確認
        paths_str = e.data
        paths = get_paths_tuple(separator, paths_str)
        space_slash_in_path_is_valid = []
        for p in paths:
            space_slash_in_path_is_valid.append(os.path.exists(p))

        if False not in space_slash_in_path_is_valid:
            paths_str = e.data.replace(' /', '}/')
            paths = get_paths_tuple(separator, paths_str)
    else:
        paths_str = e.data
        paths = get_paths_tuple(separator, paths_str)
    return paths


def get_paths_tuple(separator, paths_str):
    d = separator
    paths = tuple(s for s in paths_str.replace('{', d).replace('}', d).split(d) if s.strip() != '')
    return paths
