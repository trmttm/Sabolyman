import abc


class UseCase(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass
