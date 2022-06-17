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

    mail_template = {}
    mail_templates = {'Templates': mail_template}
    path = '/Users/yamaka/Documents/Sabolyman/Email Template'
    file_names = (
        'Japanese external standard.txt',
        'Japanese internal polite.txt',
        'Japanese internal standard.txt',
    )
    for file_name in file_names:
        mail_template.update({file_name: lambda f=f'{path}/{file_name}': interactor.create_email(f)})
    menu_injected = {
        'Mail': mail_templates,
    }
    Controller.menu_bar.configure_menu_bar(app, interactor, entities, menu_injected)
    Controller.keyboard.configure_keyboard_shortcut(app, interactor)
    app.attach_to_event_upon_closing(lambda: interactor.close(lambda: app.close('root')))

    app.launch_app()
