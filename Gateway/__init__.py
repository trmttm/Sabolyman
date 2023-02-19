import importlib.resources
import json
import os
import pickle
from typing import Iterable
from typing import Tuple
from typing import Union

import Utilities

from . import csv_exporter
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

    def load_json(self, path) -> Union[dict, None]:
        try:
            with open(path, 'rb') as f:
                return json.load(f)
        except:
            return None
    @property
    def home_folder(self) -> str:
        return os.path.join(Utilities.documents, f'Sabolyman')

    @property
    def state_folder(self) -> str:
        return os.path.join(Utilities.documents, f'Sabolyman', self._user_name)

    @property
    def script_json_path(self) -> str:
        return os.path.join(Utilities.documents, f'Sabolyman', "script_path.json")

    @property
    def graph_folder(self) -> str:
        return os.path.join(Utilities.documents, f'Sabolyman', 'Graph')

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

    def export_data_as_csv(self, file_name: str, data: Iterable):
        csv_exporter.execute(file_name, data)
