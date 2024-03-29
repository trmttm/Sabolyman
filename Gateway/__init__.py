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
        self._root_path = Utilities.documents

    def set_root_path(self, path: str):
        self._root_path = path

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
        except Exception as e:
            print(f'Failed to load json file {path} {e}')
            return None

    @property
    def root_path(self):
        return self._root_path

    @property
    def home_folder(self) -> str:
        return os.path.join(self._root_path, f'Sabolyman')

    @property
    def state_folder(self) -> str:
        return os.path.join(self._root_path, f'Sabolyman', self._user_name)

    @property
    def color_options_json_path(self) -> str:
        return os.path.join(self._root_path, f'Sabolyman', "color_options.json")

    @property
    def script_json_path(self) -> str:
        return os.path.join(self._root_path, f'Sabolyman', "script_path.json")

    @property
    def graph_folder_path(self) -> str:
        return os.path.join(self._root_path, f'Sabolyman', 'Graph')

    @property
    def gantt_chart_folder_path(self) -> str:
        return os.path.join(self._root_path, f'Sabolyman', 'Gantt Chart')

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
    def keyboard_config_folder_path(self) -> str:
        return os.path.join(self.home_folder, 'Keyboard Shortcut')

    @property
    def auto_save_path(self) -> str:
        return os.path.join(self.state_folder, 'save.sb')

    def export_data_as_csv(self, file_name: str, data: Iterable):
        csv_exporter.execute(file_name, data)

    def adjust_uri_base(self, uri: str) -> str:
        if '/MEGA/' in uri:
            uri = os.path.join(self.root_path, uri.split('/MEGA/')[1])
        return uri
