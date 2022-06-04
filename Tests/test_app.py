import unittest


class MyTestCase(unittest.TestCase):
    def test_add_card(self):
        from view_tkinter import View
        from Entities import Entities
        from Interactor import Interactor
        from Presenters import Presenters
        from Gateway import Gateway
        from Controller import configure_controller

        gui_selected = 'gui.fmide_gui'

        app = View()
        entities = Entities()
        presenters = Presenters(app)
        gateway = Gateway()
        interactor = Interactor(entities, presenters, gateway)
        interactor.load_gui(gui_selected)
        presenters.set_up_after_gui()

        configure_controller(app, interactor)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
