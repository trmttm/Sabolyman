import unittest


class MyTestCase(unittest.TestCase):
    def test_list_of_balls(self):
        import GUI
        view_model = GUI.list_of_balls.get_view_model('root')

        from view_tkinter import View
        view = View()
        view.add_widgets(view_model)
        view.launch_app()

    def test_gui_create_card(self):
        import GUI
        view_model = GUI.create_card.get_view_model('root')

        from view_tkinter import View
        view = View()
        view.add_widgets(view_model)
        view.launch_app()


if __name__ == '__main__':
    unittest.main()
