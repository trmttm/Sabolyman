import Controller.controller
import Controller.keyboard
import Controller.keyboard_shortcut_menu
import Controller.menu_bar
from Entities import Entities
from Gateway import Gateway
from Interactor import Interactor
from Presenters import Presenters
from view_tkinter import View


def start_app(gui_selected='gui01.gui', root_path: str = None):
    # Instantiation
    app = View(width=900, height=960, fullscreen=True)
    entities = Entities()
    presenters = Presenters(app)
    gateway = Gateway(entities.user.name)
    interactor = Interactor(entities, presenters, gateway)
    if root_path is not None:
        interactor.set_root_path(root_path)

    # GUI Loading
    app.set_title('Sabolyman')
    interactor.load_gui(gui_selected)
    presenters.set_up_after_gui()
    interactor.set_up()
    # Widget command mapping
    Controller.controller.configure_controller(app, interactor)
    # Menu bar
    decorate_setting_menu = Controller.keyboard_shortcut_menu.create_decorator_setting_menu(app, entities, interactor)

    def callback_configure_menu(menu_injected: dict):
        Controller.menu_bar.configure_menu_bar(app, interactor, entities, decorate_setting_menu(menu_injected))

    interactor.create_mail_menu(app.select_folder, callback_configure_menu)
    # Keyboard shortcut
    Controller.keyboard.configure_keyboard_shortcut(app, interactor, entities)
    # Teardown
    app.attach_to_event_upon_closing(lambda: interactor.close(lambda: app.close('root')))

    app.set_exception_catcher(interactor.upon_exception)

    def change_gui(gui_name):
        interactor.close(lambda: app.close('root'))
        start_app(gui_name)

    interactor.change_gui = change_gui
    app.launch_app()
