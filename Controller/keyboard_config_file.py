import os

import gui
import os_identifier
from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap

from Entities import EntitiesABC
from Interactor import InteractorABC
from .commands import get_command_name_to_command

key_text_to_key_combo_element = {
    'none': KeyMap.none,
    'shift': KeyMap.shift,
    'control': KeyMap.control,
    'command': KeyMap.command,
    'alt_option': KeyMap.alt_option,
    'function': KeyMap.function,
    KeyMap.a: KeyMap.a,
    KeyMap.b: KeyMap.b,
    KeyMap.c: KeyMap.c,
    KeyMap.d: KeyMap.d,
    KeyMap.e: KeyMap.e,
    KeyMap.f: KeyMap.f,
    KeyMap.g: KeyMap.g,
    KeyMap.h: KeyMap.h,
    KeyMap.i: KeyMap.i,
    KeyMap.j: KeyMap.j,
    KeyMap.k: KeyMap.k,
    KeyMap.l: KeyMap.l,
    KeyMap.m: KeyMap.m,
    KeyMap.n: KeyMap.n,
    KeyMap.o: KeyMap.o,
    KeyMap.p: KeyMap.p,
    KeyMap.q: KeyMap.q,
    KeyMap.r: KeyMap.r,
    KeyMap.s: KeyMap.s,
    KeyMap.t: KeyMap.t,
    KeyMap.u: KeyMap.u,
    KeyMap.v: KeyMap.v,
    KeyMap.w: KeyMap.w,
    KeyMap.x: KeyMap.x,
    KeyMap.y: KeyMap.y,
    KeyMap.z: KeyMap.z,

    KeyMap.f1: KeyMap.f1,
    KeyMap.f2: KeyMap.f2,
    KeyMap.f3: KeyMap.f3,
    KeyMap.f4: KeyMap.f4,
    KeyMap.f5: KeyMap.f5,
    KeyMap.f6: KeyMap.f6,
    KeyMap.f7: KeyMap.f7,
    KeyMap.f8: KeyMap.f8,
    KeyMap.f9: KeyMap.f9,
    KeyMap.f10: KeyMap.f10,
    KeyMap.f11: KeyMap.f11,
    KeyMap.f12: KeyMap.f12,

    KeyMap.one: KeyMap.one,
    KeyMap.two: KeyMap.two,
    KeyMap.three: KeyMap.three,
    KeyMap.four: KeyMap.four,
    KeyMap.five: KeyMap.five,
    KeyMap.six: KeyMap.six,
    KeyMap.seven: KeyMap.seven,
    KeyMap.eight: KeyMap.eight,
    KeyMap.nine: KeyMap.nine,
    KeyMap.zero: KeyMap.zero,

    KeyMap.minus: KeyMap.minus,
    KeyMap.equal: KeyMap.equal,
    KeyMap.slash: KeyMap.slash,
    KeyMap.enter: KeyMap.enter,
    KeyMap.return_: KeyMap.return_,
    KeyMap.back_space: KeyMap.back_space,
    KeyMap.delete: KeyMap.delete,
    KeyMap.escape: KeyMap.escape,

    KeyMap.up: KeyMap.up,
    KeyMap.down: KeyMap.down,
    KeyMap.left: KeyMap.left,
    KeyMap.right: KeyMap.right,
}


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC, e: EntitiesABC):
    command_name_to_command = get_command_name_to_command(app, i, e)

    i.set_active_keymap('default')

    if os_identifier.is_mac:
        file_path = os.path.join(i.keyboard_config_folder_path, 'keyboard_shortcut_config_mac.json')
    else:
        file_path = 'keyboard_shortcut_config_windows.json'

    try:
        method_to_key_combo = gui.load_shortcut_configuration_file(file_path)
    except FileNotFoundError:
        method_to_key_combo = {}

    for method_name, key_combo_str in method_to_key_combo.items():
        key_combo_list = []
        modifier = 0
        for element in key_combo_str.split(','):
            key = key_text_to_key_combo_element.get(element.lower(), None)
            if type(key) == int:
                modifier += key
            else:
                key_combo_list.append(key)
        key_combo_list.insert(0, modifier)
        key_combo = tuple(key_combo_list)
        method = command_name_to_command.get(method_name, lambda: print(method_name))
        i.add_new_keyboard_shortcut(key_combo, (method, ''))

    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def handler(k: KeyMapsABC, modifier, key):
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
