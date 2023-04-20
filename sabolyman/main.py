from view_tkinter import View

import Controller.controller
import Controller.keyboard
import Controller.keyboard_config_file
import Controller.keyboard_shortcut_menu
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

    decorate_setting_menu = Controller.keyboard_shortcut_menu.create_setting_menu(app, entities, interactor)

    def callback_configure_menu(menu_injected: dict):
        Controller.menu_bar.configure_menu_bar(app, interactor, entities, decorate_setting_menu(menu_injected))

    interactor.create_mail_menu(app.select_folder, callback_configure_menu)
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
