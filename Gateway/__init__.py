import importlib.resources
import pickle
from typing import Tuple

import Utilities

from .abc import GatewayABC


class Gateway(GatewayABC):

    def save_file(self, file_name: str, data):
        with open(file_name, 'wb') as f:
            pickle.dump(data, f)

    def load_file(self, file_name: str):
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
        return data

    @staticmethod
    def load_file_from_package(file_name: str, package_name: str):
        try:
            with importlib.resources.open_binary(package_name, file_name) as f:
                data = pickle.load(f)
        except FileNotFoundError:
            data = None
        return data

    def read_text_file(self, file_name: str, package_name: str) -> str:
        with importlib.resources.open_text(package_name, file_name) as f:
            lines = f.read()
        return lines

    def get_files_in_the_folder(self, folder_path: str, specified_extension: str = '') -> Tuple[str, ...]:
        folder_path = get_proper_path_depending_on_development_or_distribution(folder_path)
        return tuple(Utilities.get_files_in_the_folder(folder_path, specified_extension))


def get_proper_path_depending_on_development_or_distribution(relative_path):
    import os, sys
    possible_overlap = relative_path.split('/')[0]
    folder_path = os.path.join(sys.path[0], relative_path)
    if possible_overlap != '':
        folder_path = remove_overlap(folder_path, possible_overlap)
    if not (os.path.exists(folder_path)):
        folder_path = f'{os.getcwd()}/{relative_path}'
    if possible_overlap != '':
        folder_path = remove_overlap(folder_path, possible_overlap)
    return folder_path


def remove_overlap(folder_path, possible_overlap):
    return folder_path.replace(f'{possible_overlap}/{possible_overlap}', possible_overlap)
