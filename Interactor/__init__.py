from typing import Tuple

from Entities import EntitiesABC
from Gateway.abc import GatewayABC
from Presenters import PresentersABC
from . import add_new_action
from . import add_new_card
from . import delete_selected_actions
from . import delete_selected_my_cards
from . import delete_selected_their_cards
from . import load_gui
from . import load_state_from_file
from . import move_actions_down
from . import move_actions_up
from . import move_my_cards_down
from . import move_my_cards_up
from . import move_their_cards_down
from . import move_their_cards_up
from . import set_action_description
from . import set_action_is_done_or_not
from . import set_action_name
from . import set_action_owner
from . import set_action_time_expected
from . import set_card_name
from . import set_dead_line
from . import show_action_information
from . import show_my_card_information
from . import show_their_card_information
from .abc import InteractorABC
from .present_action_list import present_action_list
from .present_my_card_list import present_my_card_list
from .present_their_card_list import present_their_card_list


class Interactor(InteractorABC):

    def __init__(self, entities: EntitiesABC, presenters: PresentersABC, gateway: GatewayABC):
        self._entities = entities
        self._presenters = presenters
        self._gateway = gateway

    # GUI
    def load_gui(self, gui_name: str):
        load_gui.execute(self._entities, self._presenters, self._gateway, gui_name)

    # Save
    def save_to_file(self, file_name: str):
        self._gateway.save_file(file_name, self._entities.state)

    def load_state_from_file(self, file_name: str):
        load_state_from_file.execute(self._entities, self._gateway, self._presenters, file_name)

    # Cards
    def add_new_card(self):
        add_new_card.execute(self._entities, self._presenters)

    def delete_selected_my_cards(self, indexes: Tuple[int]):
        delete_selected_my_cards.execute(self._entities, self._presenters, indexes, self._entities.my_cards)

    def delete_selected_their_cards(self, indexes: Tuple[int]):
        delete_selected_their_cards.execute(self._entities, self._presenters, indexes, self._entities.their_cards)

    def set_card_name(self, card_name: str):
        set_card_name.execute(self._entities, self._presenters, card_name)

    def set_dead_line(self, dead_line_str: str):
        set_dead_line.execute(self._entities, self._presenters, dead_line_str)

    def add_new_action(self):
        add_new_action.execute(self._entities, self._presenters)

    def delete_selected_actions(self, indexes: Tuple[int]):
        delete_selected_actions.execute(self._entities, self._presenters, indexes)

    def show_my_card_information(self, indexes: Tuple[int]):
        show_my_card_information.execute(self._entities, self._presenters, indexes)

    def show_their_card_information(self, indexes: Tuple[int]):
        show_their_card_information.execute(self._entities, self._presenters, indexes)

    def move_my_cards_up(self, indexes: Tuple[int, ...]):
        move_my_cards_up.execute(self._entities, self._presenters, indexes)

    def move_my_cards_down(self, indexes: Tuple[int, ...]):
        move_my_cards_down.execute(self._entities, self._presenters, indexes)

    def move_their_cards_up(self, indexes: Tuple[int, ...]):
        move_their_cards_up.execute(self._entities, self._presenters, indexes)

    def move_their_cards_down(self, indexes: Tuple[int, ...]):
        move_their_cards_down.execute(self._entities, self._presenters, indexes)

    # Action
    def set_action_name(self, action_name: str):
        set_action_name.execute(self._entities, self._presenters, action_name)

    def set_action_owner(self, owner_name: str):
        set_action_owner.execute(self._entities, self._presenters, owner_name)

    def set_action_is_done_or_not(self, done_or_not: bool):
        set_action_is_done_or_not.execute(self._entities, self._presenters, done_or_not)

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
