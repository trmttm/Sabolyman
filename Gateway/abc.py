import abc
from typing import Iterable
from typing import Tuple
from typing import Union


class GatewayABC(abc.ABC):
    @abc.abstractmethod
    def set_root_path(self, path: str):
        pass

    @abc.abstractmethod
    def save_file(self, file_name: str, data):
        pass

    @abc.abstractmethod
    def load_file(self, file_name: str):
        pass

    @staticmethod
    @abc.abstractmethod
    def load_file_from_package(file_name: str, package_name: str):
        pass

    @abc.abstractmethod
    def read_text_file(self, file_name: str, package_name: str) -> str:
        pass

    @abc.abstractmethod
    def get_files_in_the_folder(self, folder_path: str, specified_extension: str = '') -> Tuple[str, ...]:
        pass

    @property
    @abc.abstractmethod
    def home_folder(self) -> str:
        pass

    @abc.abstractmethod
    def load_json(self, path) -> Union[dict, None]:
        pass

    @property
    @abc.abstractmethod
    def script_json_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def color_options_json_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def state_folder(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def gantt_chart_folder_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def graph_folder_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def mail_template_package(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def mail_template_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def cards_template_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def keyboard_config_folder_path(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def auto_save_path(self) -> str:
        pass

    @abc.abstractmethod
    def export_data_as_csv(self, file_name: str, data: Iterable):
        pass
