from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap

from Interactor import InteractorABC


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC):
    i.set_active_keymap('default')
    f = i.add_new_keyboard_shortcut

    f((KeyMap.command, KeyMap.w), (lambda: i.close(lambda: app.close('root')), ''))
    f((KeyMap.command, KeyMap.d), (lambda: i.duplicate_selected_card(), ''))

    # i.set_active_keymap('special')
    # f((KeyMap.command, KeyMap.a), (lambda: print('Hello!'), ''))
    # f((KeyMap.command, KeyMap.s), (lambda: i.set_active_keymap('default'), 'switched'))

    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def handler(k: KeyMapsABC, modifier, key):
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
