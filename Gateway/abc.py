import abc


class GatewayABC(abc.ABC):
    @abc.abstractmethod
    def save_file(self, file_name: str, data):
        pass

    @abc.abstractmethod
    def load_file(self, file_name: str):
        pass
