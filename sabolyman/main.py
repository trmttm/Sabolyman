from view_tkinter import View

import Controller.controller
import Controller.keyboard
import Controller.menu_bar
import WidgetNames
from Entities import Entities
from Gateway import Gateway
from Interactor import Interactor
from Presenters import Presenters


def start_app(gui_selected='gui01.gui'):
    # Instantiation
    app = View(width=900, height=960)
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
    app.bind_tree_enter(lambda: app.focus('root'), WidgetNames.tree_card_actions)
    # Menu bar
    f = app.select_folder
    j = Controller.menu_bar.configure_menu_bar
    interactor.create_mail_menu(f, lambda menu_injected: j(app, interactor, entities, menu_injected))
    # Keyboard shortcut
    Controller.keyboard.configure_keyboard_shortcut(app, interactor, entities)
    # Teardown
    app.attach_to_event_upon_closing(lambda: interactor.close(lambda: app.close('root')))

    app.launch_app()
