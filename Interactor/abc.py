import abc


class InteractorABC(abc.ABC):
    @abc.abstractmethod
    def add_new_card(self):
        pass

    @abc.abstractmethod
    def delete_selected_cards(self):
        pass

    @abc.abstractmethod
    def show_card_information(self):
        pass

    @abc.abstractmethod
    def set_card_name(self):
        pass

    @abc.abstractmethod
    def set_dead_line(self):
        pass
