import gui
from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC

from Entities import EntitiesABC
from Interactor import InteractorABC
from . import keyboard_config_file


def create_setting_menu(app: ViewABC, entities: EntitiesABC, interactor: InteractorABC):
    file_path = keyboard_config_file.get_file_path(interactor)
    command_names = keyboard_config_file.get_method_name_to_key_combo(app, interactor, entities).keys()
    n_commands = len(command_names)
    specified_parent = 'pop_up_shortcut_setting'
    title = 'Filter setting'
    width = 1000
    height = 500
    options = top_level_options(title, (width, height))

    def get_view_model_shortcut_setting():
        view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
        commands_to_short_cuts = keyboard_config_file.get_method_name_to_key_combo(app, interactor, entities)
        return view_model + gui.create_view_model_of_shortcut_setter(callback, commands_to_short_cuts, specified_parent)

    def save_commands():
        data = dict(zip(command_names, gui.get_state(app, n_commands)))
        gui.save_shortcut_configuration_file(file_path, data)
        keyboard_config_file.configure_keyboard_shortcut(app, interactor, entities)

    def callback(command_str):
        print(command_str, gui.get_state(app, n_commands))
        if command_str == gui.KEY_CANCEL:
            app.close(specified_parent)
        elif command_str == gui.KEY_APPLY:
            save_commands()
        elif command_str == gui.KEY_DONE:
            save_commands()
            app.close(specified_parent)

    def menu_wrapper(menu_injected: dict):
        def open_keyboard_shortcut_setting():
            app.add_widgets(get_view_model_shortcut_setting())
            [gui.bind_commands(n, app) for n in range(n_commands)]

        injected_menu = {
            'Setting': {
                'Keyboard shortcut': lambda: open_keyboard_shortcut_setting(),
            }, }
        menu_injected.update(injected_menu)
        return menu_injected

    return menu_wrapper
