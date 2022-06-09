from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap

from Interactor import InteractorABC


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC):
    i.set_active_keymap('default')
    i.add_new_keyboard_shortcut((KeyMap.command, KeyMap.l), (lambda: i.load_state_from_file(f'save.sb'), ''))
    i.add_new_keyboard_shortcut((KeyMap.command, KeyMap.s), (lambda: i.save_to_file(f'save.sb'), ''))

    # i.set_active_keymap('special')
    # i.add_new_keyboard_shortcut((KeyMap.command, KeyMap.a), (lambda: print('Hello!'), ''))
    # i.add_new_keyboard_shortcut((KeyMap.command, KeyMap.s), (lambda: i.set_active_keymap('default'), 'switched'))

    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def handler(k: KeyMapsABC, modifier, key):
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
