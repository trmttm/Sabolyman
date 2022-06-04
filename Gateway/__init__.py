import pickle

from .abc import GatewayABC


class Gateway(GatewayABC):

    def load_file(self, file_name: str):
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
        return data
