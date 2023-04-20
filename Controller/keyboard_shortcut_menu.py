from interface_view import ViewABC

from Entities.abc_entities import EntitiesABC
from Interactor.abc import InteractorABC
from .commands import open_keyboard_shortcut_setting


def create_decorator_setting_menu(app: ViewABC, entities: EntitiesABC, interactor: InteractorABC):
    def menu_wrapper(menu_injected: dict):
        injected_menu = {
            'Setting': {
                'Keyboard shortcut': lambda: open_keyboard_shortcut_setting(app, interactor, entities),
            }, }
        menu_injected.update(injected_menu)
        return menu_injected

    return menu_wrapper
