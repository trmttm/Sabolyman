from view_tkinter import View

import Controller as controller
from Entities import Entities
from Gateway import Gateway
from Interactor import Interactor
from Presenters import Presenters


def start_app(gui_selected='gui01.gui'):
    app = View(width=900, height=960)
    app.set_title('Sabolyman')
    entities = Entities()
    presenters = Presenters(app)
    gateway = Gateway()
    interactor = Interactor(entities, presenters, gateway)
    # Configuration
    interactor.load_gui(gui_selected)
    presenters.set_up_after_gui()
    controller.configure_controller(app, interactor)
    controller.configure_menu_bar(app, interactor, entities)
    app.launch_app()
