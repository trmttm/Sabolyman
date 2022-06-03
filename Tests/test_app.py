import unittest


class MyTestCase(unittest.TestCase):
    def test_add_card(self):
        import datetime
        import pickle
        from view_tkinter import View
        from Entities import Entities
        from Interactor import Interactor
        from Presenters import Presenters

        app = View()
        entities = Entities()
        presenters = Presenters(app)
        i = Interactor(entities, presenters, app)

        with open('gui.fmide_gui', 'rb') as f:
            view_model = pickle.load(f)


        app.add_widgets(view_model)

        name = 'my_balls'
        select_nth = 0
        presenters.update_cards(('Card1',), (datetime.datetime.today(),), select_nth)

        app.bind_command_to_widget(f'btn_{name}_add', lambda: i.add_new_card())
        app.bind_command_to_widget(f'btn_{name}_delete', lambda: i.delete_selected_cards())
        app.bind_command_to_widget('tree_my_balls', lambda: i.show_card_information())
        app.bind_command_to_widget('entry_name', lambda *_: i.set_card_name())
        app.bind_command_to_widget('entry_dead_line', lambda *_: i.set_dead_line())

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
