from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap

from Interactor import InteractorABC
from . import state


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC):
    i.set_active_keymap('default')
    f = i.add_new_keyboard_shortcut

    f((KeyMap.command, KeyMap.w), (lambda: i.close(lambda: app.close('root')), ''))
    f((KeyMap.command, KeyMap.d), (lambda: i.duplicate_selected_card(), ''))
    f((KeyMap.command, KeyMap.c), (lambda: i.set_color_to_cards(state.get_my_cards_selected_indexes(app),
                                                                state.get_their_cards_selected_indexes(app),
                                                                app.ask_color()), ''))

    # i.set_active_keymap('special')
    # f((KeyMap.command, KeyMap.a), (lambda: print('Hello!'), ''))
    # f((KeyMap.command, KeyMap.s), (lambda: i.set_active_keymap('default'), 'switched'))

    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def handler(k: KeyMapsABC, modifier, key):
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
