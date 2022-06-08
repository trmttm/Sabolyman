def start_app(gui_selected='gui01.gui'):
    from view_tkinter import View
    from Entities import Entities
    from Interactor import Interactor
    from Presenters import Presenters
    from Gateway import Gateway
    import Controller as controller
    app = View(width=900, height=960)
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
