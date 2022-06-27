import importlib.resources
import os
import pickle
from typing import Tuple

import Utilities

from .abc import GatewayABC


class Gateway(GatewayABC):
    def __init__(self, user_name):
        self._user_name = user_name

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
        folder_path = Utilities.get_proper_path_depending_on_development_or_distribution(folder_path)
        return tuple(Utilities.get_files_in_the_folder(folder_path, specified_extension))

    @property
    def home_folder(self) -> str:
        return os.path.join(Utilities.documents, f'Sabolyman')

    @property
    def state_folder(self) -> str:
        return os.path.join(Utilities.documents, f'Sabolyman', self._user_name)

    @property
    def mail_template_package(self) -> str:
        return 'Resources.Mail'

    @property
    def mail_template_path(self) -> str:
        return 'Resources/Mail'

    @property
    def cards_template_path(self) -> str:
        return os.path.join(self.home_folder, 'Card Template')

    @property
    def auto_save_path(self) -> str:
        return os.path.join(self.state_folder, 'save.sb')
