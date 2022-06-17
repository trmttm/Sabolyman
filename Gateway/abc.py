import abc


class GatewayABC(abc.ABC):
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
    def read_text_file(self, file_name: str) -> str:
        pass
