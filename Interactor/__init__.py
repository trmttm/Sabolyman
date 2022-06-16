from typing import Tuple

from keyboard_shortcut import KeyMaps

from Entities import EntitiesABC
from Gateway.abc import GatewayABC
from Presenters import PresentersABC
from . import add_new_action
from . import add_new_card
from . import add_template_card
from . import delete_selected_actions
from . import delete_selected_my_cards
from . import delete_selected_their_cards
from . import duplicate_selected_card
from . import get_card_index
from . import load_gui
from . import load_state_from_file
from . import mark_action_completed
from . import move_actions_down
from . import move_actions_up
from . import move_my_cards_down
from . import move_my_cards_up
from . import move_their_cards_down
from . import move_their_cards_up
from . import present_action_list
from . import present_card_list
from . import save_as_template_card
from . import set_action_complete_time
from . import set_action_description
from . import set_action_is_done_or_not
from . import set_action_name
from . import set_action_owner
from . import set_action_time_expected
from . import set_card_client
from . import set_card_name
from . import set_dead_line
from . import show_action_information
from . import show_my_card_information
from . import show_their_card_information
from .abc import InteractorABC


class Interactor(InteractorABC):

    def __init__(self, entities: EntitiesABC, presenters: PresentersABC, gateway: GatewayABC):
        self._entities = entities
        self._presenters = presenters
        self._gateway = gateway
        self._keymaps = KeyMaps()

    # GUI
    def load_gui(self, gui_name: str):
        load_gui.execute(self._entities, self._presenters, self._gateway, gui_name)

    # Save
    def save_to_file(self, file_name: str):
        self._gateway.save_file(file_name, self._entities.state)

    def load_state_from_file(self, file_name: str):
        load_state_from_file.execute(self._entities, self._gateway, self._presenters, file_name)

    def save_as_template_card(self, file_name: str):
        save_as_template_card.execute(self._entities, self._gateway, file_name)

    def add_template_card(self, file_name: str):
        add_template_card.execute(self._entities, self._gateway, self._presenters, file_name)

    # Cards
    def add_new_card(self):
        add_new_card.execute(self._entities, self._presenters)

    def duplicate_selected_card(self):
        duplicate_selected_card.execute(self._entities, self._presenters, self._entities.active_card)

    def delete_selected_my_cards(self, indexes: Tuple[int]):
        delete_selected_my_cards.execute(self._entities, self._presenters, indexes, self._entities.my_cards)

    def delete_selected_their_cards(self, indexes: Tuple[int]):
        delete_selected_their_cards.execute(self._entities, self._presenters, indexes, self._entities.their_cards)

    def set_card_name(self, card_name: str):
        set_card_name.execute(self._entities, self._presenters, card_name)

    def set_dead_line(self, dead_line_str: str):
        set_dead_line.execute(self._entities, self._presenters, dead_line_str)

    def set_client(self, client_name: str):
        set_card_client.execute(self._entities, self._presenters, client_name)

    def add_new_action(self):
        add_new_action.execute(self._entities, self._presenters)

    def delete_selected_actions(self, indexes: Tuple[int]):
        delete_selected_actions.execute(self._entities, self._presenters, indexes)

    def show_my_card_information(self, indexes: Tuple[int]):
        indexes = get_card_index.execute(self._entities, self._entities.my_cards, indexes)
        show_my_card_information.execute(self._entities, self._presenters, indexes)

    def show_their_card_information(self, indexes: Tuple[int]):
        indexes = get_card_index.execute(self._entities, self._entities.their_cards, indexes)
        show_their_card_information.execute(self._entities, self._presenters, indexes)

    def move_my_cards_up(self, indexes: Tuple[int, ...]):
        move_my_cards_up.execute(self._entities, self._presenters, indexes)

    def move_my_cards_down(self, indexes: Tuple[int, ...]):
        move_my_cards_down.execute(self._entities, self._presenters, indexes)

    def move_their_cards_up(self, indexes: Tuple[int, ...]):
        move_their_cards_up.execute(self._entities, self._presenters, indexes)

    def move_their_cards_down(self, indexes: Tuple[int, ...]):
        move_their_cards_down.execute(self._entities, self._presenters, indexes)

    def set_color_to_cards(self, indexes1: Tuple[int, ...], indexes2: Tuple[int, ...], color):
        active_card = self._entities.active_card
        if active_card in self._entities.my_cards:
            self.set_color_to_my_cards(indexes1, color)
        elif active_card in self._entities.their_cards:
            self.set_color_to_their_cards(indexes2, color)

    def set_color_to_my_cards(self, indexes: Tuple[int, ...], color):
        self._set_color_to_cards(self._entities.get_my_cards_by_indexes(indexes), color)

    def set_color_to_their_cards(self, indexes: Tuple[int, ...], color):
        self._set_color_to_cards(self._entities.get_their_cards_by_indexes(indexes), color)

    def _set_color_to_cards(self, cards, color):
        for card in cards:
            card.set_color(color)
        present_card_list.execute(self._entities, self._presenters)

    # Action
    def set_action_name(self, action_name: str):
        set_action_name.execute(self._entities, self._presenters, action_name)

    def set_action_owner(self, owner_name: str):
        set_action_owner.execute(self._entities, self._presenters, owner_name)

    def mark_action_completed(self, done_or_not: bool):
        mark_action_completed.execute(self._entities, self._presenters, done_or_not)

    def set_action_complete_time(self, done_or_not: bool):
        set_action_complete_time.execute(self._entities, done_or_not)
        present_action_list.execute(self._entities, self._presenters)

    def set_action_description(self, description: str):
        set_action_description.execute(self._entities, self._presenters, description)

    def set_action_time_expected(self, time_expected: str):
        set_action_time_expected.execute(self._entities, self._presenters, time_expected)

    def show_action_information(self, indexes: Tuple[int]):
        show_action_information.execute(self._entities, self._presenters, indexes)

    def move_actions_up(self, indexes: Tuple[int, ...]):
        move_actions_up.execute(self._entities, self._presenters, indexes)

    def move_actions_down(self, indexes: Tuple[int, ...]):
        move_actions_down.execute(self._entities, self._presenters, indexes)

    # Keyboard shortcut
    def set_active_keymap(self, name: str):
        self._keymaps.set_active_keymap(name)

    def add_new_keyboard_shortcut(self, key_combo: tuple, command_and_feedback: tuple):
        self._keymaps.active_keymap.add_new_keyboard_shortcut(key_combo, command_and_feedback)

    @property
    def keymaps(self) -> KeyMaps:
        return self._keymaps

    # Setup Teardown
    def set_up(self):
        loaded = True
        try:
            self.load_state_from_file('save.sb')
        except:
            loaded = False
        if loaded:
            self.show_my_card_information((0,))
            self.show_their_card_information((0,))
            self.show_action_information((0,))

    def close(self, command):
        self.save_to_file('save.sb')
        command()
