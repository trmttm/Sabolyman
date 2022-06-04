import abc


class GatewayABC(abc.ABC):
    @abc.abstractmethod
    def load_file(self, file_name: str):
        pass
