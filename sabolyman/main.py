import gui
from interface_tk import top_level_options
from interface_tk import widget_model
from view_tkinter import View

import Controller.controller
import Controller.keyboard
import Controller.keyboard_config_file
import Controller.menu_bar
from Entities import Entities
from Gateway import Gateway
from Interactor import Interactor
from Presenters import Presenters


def start_app(gui_selected='gui01.gui'):
    # Instantiation
    app = View(width=900, height=960, fullscreen=True)
    entities = Entities()
    presenters = Presenters(app)
    gateway = Gateway(entities.user.name)
    interactor = Interactor(entities, presenters, gateway)

    # GUI Loading
    app.set_title('Sabolyman')
    interactor.load_gui(gui_selected)
    presenters.set_up_after_gui()
    interactor.set_up()
    # Widget command mapping
    Controller.controller.configure_controller(app, interactor)
    # Menu bar
    f = app.select_folder
    j = Controller.menu_bar.configure_menu_bar

    file_path = Controller.keyboard_config_file.get_file_path(interactor)
    command_names = Controller.keyboard_config_file.get_method_name_to_key_combo(app, interactor, entities).keys()
    n_commands = len(command_names)

    specified_parent = 'pop_up_shortcut_setting'
    title = 'Filter setting'
    width = 1000
    height = 500
    options = top_level_options(title, (width, height))

    def get_view_model_shortcut_setting():
        view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
        commands_to_short_cuts = Controller.keyboard_config_file.get_method_name_to_key_combo(app, interactor, entities)
        return view_model + gui.create_view_model_of_shortcut_setter(callback, commands_to_short_cuts, specified_parent)

    def save_commands():
        data = dict(zip(command_names, gui.get_state(app, n_commands)))
        gui.save_shortcut_configuration_file(file_path, data)
        Controller.keyboard_config_file.configure_keyboard_shortcut(app, interactor, entities)

    def callback(command_str):
        print(command_str, gui.get_state(app, n_commands))
        if command_str == gui.KEY_CANCEL:
            app.close(specified_parent)
        elif command_str == gui.KEY_APPLY:
            save_commands()
        elif command_str == gui.KEY_DONE:
            save_commands()
            app.close(specified_parent)

    def menu_wrapper(menu_data: dict):
        def open_keyboard_shortcut_setting():
            app.add_widgets(get_view_model_shortcut_setting())
            [gui.bind_commands(n, app) for n in range(n_commands)]

        injected_menu = {
            'Setting': {
                'Keyboard shortcut': lambda: open_keyboard_shortcut_setting(),
            }, }
        menu_data.update(injected_menu)
        return menu_data

    interactor.create_mail_menu(f, lambda menu_injected: j(app, interactor, entities, menu_wrapper(menu_injected)))
    # Keyboard shortcut
    configure_shortcut_by_file = True
    if configure_shortcut_by_file:
        Controller.keyboard_config_file.configure_keyboard_shortcut(app, interactor, entities)
    else:
        Controller.keyboard.configure_keyboard_shortcut(app, interactor, entities)
    # Teardown
    app.attach_to_event_upon_closing(lambda: interactor.close(lambda: app.close('root')))

    def change_gui(gui_name):
        interactor.close(lambda: app.close('root'))
        start_app(gui_name)

    interactor.change_gui = change_gui
    app.launch_app()
