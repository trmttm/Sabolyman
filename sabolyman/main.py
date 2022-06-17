from view_tkinter import View

import Controller.controller
import Controller.keyboard
import Controller.menu_bar
from Entities import Entities
from Gateway import Gateway
from Interactor import Interactor
from Presenters import Presenters
from . import create_mail_menu


def start_app(gui_selected='gui01.gui'):
    # Instantiation
    app = View(width=900, height=960)
    entities = Entities()
    presenters = Presenters(app)
    gateway = Gateway()
    interactor = Interactor(entities, presenters, gateway)

    # GUI Loading
    app.set_title('Sabolyman')
    interactor.load_gui(gui_selected)
    presenters.set_up_after_gui()
    interactor.set_up()
    # Widget command mapping
    Controller.controller.configure_controller(app, interactor)
    # Menu bar
    menu_to_be_injected = create_mail_menu.execute(interactor, interactor.mail_template_path)
    Controller.menu_bar.configure_menu_bar(app, interactor, entities, menu_to_be_injected)
    # Keyboard shortcu
    Controller.keyboard.configure_keyboard_shortcut(app, interactor)
    # Teardown
    app.attach_to_event_upon_closing(lambda: interactor.close(lambda: app.close('root')))

    app.launch_app()
