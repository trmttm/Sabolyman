from interface_view import ViewABC

from Entities import EntitiesABC
from Interactor import InteractorABC
from . import keyboard_config_file
from .commands import open_keyboard_shortcut_setting


def create_decorator_setting_menu(app: ViewABC, entities: EntitiesABC, interactor: InteractorABC):
    command_names = keyboard_config_file.get_method_name_to_key_combo(app, interactor, entities).keys()
    n_commands = len(command_names)

    def menu_wrapper(menu_injected: dict):
        injected_menu = {
            'Setting': {
                'Keyboard shortcut': lambda: open_keyboard_shortcut_setting(app, interactor, entities, n_commands),
            }, }
        menu_injected.update(injected_menu)
        return menu_injected

    return menu_wrapper
