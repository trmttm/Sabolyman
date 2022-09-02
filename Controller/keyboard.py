import WidgetNames
import os_identifier
from Entities import EntitiesABC
from Interactor import InteractorABC
from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap

from . import state
from . import utilities


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC, e: EntitiesABC):
    i.set_active_keymap('default')
    f = i.add_new_keyboard_shortcut

    if os_identifier.is_mac:
        main_modifier = KeyMapk.command
        sub_modifier = KeyMap.control
    else:
        main_modifier = KeyMap.control
        sub_modifier = KeyMap.alt_option

    f((main_modifier, KeyMap.l), (lambda: i.load_state_from_file(app.select_open_file()), ''))
    f((main_modifier, KeyMap.s), (lambda: i.save_state(), ''))
    f((main_modifier + KeyMap.shift, KeyMap.s), (lambda: i.save_to_file(utilities.default_file_path(i, e)), ''))
    f((main_modifier, KeyMap.w), (lambda: i.close(lambda: app.close('root')), ''))
    f((main_modifier, KeyMap.d), (lambda: i.duplicate_selected_card(), ''))
    f((main_modifier, KeyMap.m), (lambda: i.make_email(), ''))
    f((sub_modifier, KeyMap.c), (lambda: i.set_color_to_cards(state.get_left_tree_selected_indexes(app),
                                                              state.get_right_tree_selected_indexes(app),
                                                              app.ask_color()), ''))
    f((sub_modifier, KeyMap.h), (lambda: i.toggle_hide_finished_cards(), ''))
    f((main_modifier, KeyMap.f), (lambda: app.focus(WidgetNames.entry_search_box), ''))

    f((main_modifier, KeyMap.one), (lambda: i.sort_cards_by_color(), ''))
    f((main_modifier, KeyMap.two), (lambda: i.sort_cards_by_deadline(), ''))
    f((main_modifier, KeyMap.three), (lambda: i.sort_cards_by_name(), ''))
    f((main_modifier, KeyMap.four), (lambda: i.sort_cards_by_current_owner(), ''))
    f((main_modifier, KeyMap.five), (lambda: i.sort_cards_by_current_client(), ''))

    # i.set_active_keymap('special')
    # f((KeyMap.command, KeyMap.a), (lambda: print('Hello!'), ''))
    # f((KeyMap.command, KeyMap.s), (lambda: i.set_active_keymap('default'), 'switched'))

    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def handler(k: KeyMapsABC, modifier, key):
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
