from view_tkinter import View

import Controller.controller
import Controller.keyboard
import Controller.menu_bar
from Entities import Entities
from Gateway import Gateway
from Interactor import Interactor
from Presenters import Presenters


def start_app(gui_selected='gui01.gui'):
    # Instantiation
    app = View(width=900, height=960)
    entities = Entities()
    presenters = Presenters(app)
    gateway = Gateway()
    interactor = Interactor(entities, presenters, gateway)

    # Configuration
    app.set_title('Sabolyman')
    interactor.load_gui(gui_selected)
    presenters.set_up_after_gui()
    interactor.set_up()
    Controller.controller.configure_controller(app, interactor)
    Controller.menu_bar.configure_menu_bar(app, interactor, entities)
    Controller.keyboard.configure_keyboard_shortcut(app, interactor)

    def upon_close():
        interactor.save_to_file('save.sb')
        app.close('root')
    app.attach_to_event_upon_closing(upon_close)

    app.launch_app()
