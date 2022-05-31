import unittest


def load_gui(module, parent: str = 'root'):
    view_model = module.get_view_model(parent)
    from view_tkinter import View
    view = View()
    view.add_widgets(view_model)
    view.launch_app()


class MyTestCase(unittest.TestCase):
    def test_list_of_balls(self):
        import GUI
        module = GUI.list_of_balls
        load_gui(module)

    def test_gui_create_card(self):
        import GUI
        module = GUI.create_card
        load_gui(module)

    def test_combined(self):
        import GUI
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()
        stacker.vstack(
            w.PanedWindow('pw_main', stacker).is_vertical().stackers(
                w.Label('1').text(''),
                w.Label('2').text('')
            )
        )
        view_model = stacker.view_model
        view_model += GUI.list_of_balls.get_view_model('frame_1')
        view_model += GUI.create_card.get_view_model('frame_2')
        from view_tkinter import View
        view = View()
        view.add_widgets(view_model)
        view.launch_app()


if __name__ == '__main__':
    unittest.main()
