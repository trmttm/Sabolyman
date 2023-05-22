import os

import os_identifier
import shortcut_setter
from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap
from view_tkinter.TkImplementations.keyboard_shortcut import tk_n_none  # this may be undesirable dependency to tkinter
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
    KeyMap.a.lower(): KeyMap.a,
    KeyMap.b.lower(): KeyMap.b,
    KeyMap.c.lower(): KeyMap.c,
    KeyMap.d.lower(): KeyMap.d,
    KeyMap.e.lower(): KeyMap.e,
    KeyMap.f.lower(): KeyMap.f,
    KeyMap.g.lower(): KeyMap.g,
    KeyMap.h.lower(): KeyMap.h,
    KeyMap.i.lower(): KeyMap.i,
    KeyMap.j.lower(): KeyMap.j,
    KeyMap.k.lower(): KeyMap.k,
    KeyMap.l.lower(): KeyMap.l,
    KeyMap.m.lower(): KeyMap.m,
    KeyMap.n.lower(): KeyMap.n,
    KeyMap.o.lower(): KeyMap.o,
    KeyMap.p.lower(): KeyMap.p,
    KeyMap.q.lower(): KeyMap.q,
    KeyMap.r.lower(): KeyMap.r,
    KeyMap.s.lower(): KeyMap.s,
    KeyMap.t.lower(): KeyMap.t,
    KeyMap.u.lower(): KeyMap.u,
    KeyMap.v.lower(): KeyMap.v,
    KeyMap.w.lower(): KeyMap.w,
    KeyMap.x.lower(): KeyMap.x,
    KeyMap.y.lower(): KeyMap.y,
    KeyMap.z.lower(): KeyMap.z,

    KeyMap.f1.lower(): KeyMap.f1,
    KeyMap.f2.lower(): KeyMap.f2,
    KeyMap.f3.lower(): KeyMap.f3,
    KeyMap.f4.lower(): KeyMap.f4,
    KeyMap.f5.lower(): KeyMap.f5,
    KeyMap.f6.lower(): KeyMap.f6,
    KeyMap.f7.lower(): KeyMap.f7,
    KeyMap.f8.lower(): KeyMap.f8,
    KeyMap.f9.lower(): KeyMap.f9,
    KeyMap.f10.lower(): KeyMap.f10,
    KeyMap.f11.lower(): KeyMap.f11,
    KeyMap.f12.lower(): KeyMap.f12,

    KeyMap.one.lower(): KeyMap.one,
    KeyMap.two.lower(): KeyMap.two,
    KeyMap.three.lower(): KeyMap.three,
    KeyMap.four.lower(): KeyMap.four,
    KeyMap.five.lower(): KeyMap.five,
    KeyMap.six.lower(): KeyMap.six,
    KeyMap.seven.lower(): KeyMap.seven,
    KeyMap.eight.lower(): KeyMap.eight,
    KeyMap.nine.lower(): KeyMap.nine,
    KeyMap.zero.lower(): KeyMap.zero,

    KeyMap.minus.lower(): KeyMap.minus,
    KeyMap.equal.lower(): KeyMap.equal,
    KeyMap.slash.lower(): KeyMap.slash,
    KeyMap.enter.lower(): KeyMap.enter,
    KeyMap.return_.lower(): KeyMap.return_,
    KeyMap.back_space.lower(): KeyMap.back_space,
    KeyMap.delete.lower(): KeyMap.delete,
    KeyMap.escape.lower(): KeyMap.escape,

    KeyMap.up.lower(): KeyMap.up,
    KeyMap.down.lower(): KeyMap.down,
    KeyMap.left.lower(): KeyMap.left,
    KeyMap.right.lower(): KeyMap.right,
}


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC, e: EntitiesABC):
    i.set_active_keymap('default')
    command_name_to_command = get_command_name_to_command(app, i, e)
    method_to_key_combo = get_method_name_to_key_combo(app, i, e)

    register_keyboard_shortcuts(command_name_to_command, i, method_to_key_combo)
    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def register_keyboard_shortcuts(command_name_to_command: dict, i: InteractorABC, method_to_key_combo: dict):
    i.clear_keyboard_shortcuts()
    for method_name, key_combo_str in method_to_key_combo.items():
        tk_n_none_applied_once = False
        key_combo_list = []
        modifier = 0
        for element in key_combo_str.split(','):
            key = key_text_to_key_combo_element.get(element.lower(), None)
            if type(key) == int:
                modifier += key
                if not tk_n_none_applied_once:
                    modifier += tk_n_none
                    tk_n_none_applied_once = True
            else:
                key_combo_list.append(key)
        key_combo_list.insert(0, modifier)
        key_combo = tuple(key_combo_list)
        method = command_name_to_command.get(method_name, lambda: print(method_name))
        i.add_new_keyboard_shortcut(key_combo, (method, ''))


def get_method_name_to_key_combo(v: ViewABC, i: InteractorABC, e: EntitiesABC):
    command_names = get_command_name_to_command(v, i, e).keys()

    method_to_key_combo = dict(zip(command_names, ('' for _ in command_names)))
    try:
        method_to_key_combo_from_json = shortcut_setter.load_shortcut_configuration_file(get_file_path(i))
    except FileNotFoundError:
        method_to_key_combo_from_json = {}
    method_to_key_combo.update(method_to_key_combo_from_json)
    return method_to_key_combo


def get_file_path(interactor: InteractorABC) -> str:
    if os_identifier.is_mac:
        file_path = os.path.join(interactor.keyboard_config_folder_path, 'keyboard_shortcut_config_mac.json')
    else:
        file_path = os.path.join(interactor.keyboard_config_folder_path, 'keyboard_shortcut_config_windows.json')
    return file_path


def handler(k: KeyMapsABC, modifier, key):
    if len(key) == 1:
        key = key.lower()
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
