from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap

import WidgetNames
from Entities import EntitiesABC
from Interactor import InteractorABC
from . import state
from . import utilities


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC, e: EntitiesABC):
    i.set_active_keymap('default')
    f = i.add_new_keyboard_shortcut

    f((KeyMap.command, KeyMap.l), (lambda: i.load_state_from_file(app.select_open_file()), ''))
    f((KeyMap.command, KeyMap.s), (lambda: i.save_state(), ''))
    f((KeyMap.command + KeyMap.shift, KeyMap.s),
      (lambda: i.save_to_file(app.select_save_file(initialfile=utilities.default_file_name(e))), ''))
    f((KeyMap.command, KeyMap.w), (lambda: i.close(lambda: app.close('root')), ''))
    f((KeyMap.command, KeyMap.d), (lambda: i.duplicate_selected_card(), ''))
    f((KeyMap.command, KeyMap.m), (lambda: i.make_email(), ''))
    f((KeyMap.control, KeyMap.c), (lambda: i.set_color_to_cards(state.get_my_cards_selected_indexes(app),
                                                                state.get_their_cards_selected_indexes(app),
                                                                app.ask_color()), ''))
    f((KeyMap.control, KeyMap.h), (lambda: i.toggle_hide_finished_cards(), ''))
    f((KeyMap.command, KeyMap.f), (lambda: app.focus(WidgetNames.entry_search_box), ''))

    # i.set_active_keymap('special')
    # f((KeyMap.command, KeyMap.a), (lambda: print('Hello!'), ''))
    # f((KeyMap.command, KeyMap.s), (lambda: i.set_active_keymap('default'), 'switched'))

    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def handler(k: KeyMapsABC, modifier, key):
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
