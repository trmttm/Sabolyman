from .card import Card


class CutActionManager:
    def __init__(self):
        self._cut_mode = False
        self._cutting_action_from = None

    def set_card_to_cut_action_fom(self, card: Card):
        self._cutting_action_from = card

    def get_card_to_cut_action_fom(self) -> Card:
        return self._cutting_action_from

    def turn_off_cut_mode(self):
        self._cut_mode = False
        self._cutting_action_from = None

    def turn_on_cut_mode(self):
        self._cut_mode = True

    def get_cut_mode(self) -> bool:
        return self._cut_mode
