import unittest


def load_gui(module, parent: str = 'root', **kwargs):
    view = instantiate_view(module, parent, **kwargs)
    view.launch_app()


def instantiate_view(module, parent: str = 'root', **kwargs):
    from view_tkinter import View
    view_model = module.get_view_model(parent)
    view = View(**kwargs)
    view.add_widgets(view_model)
    return view


def load_gui_from_pickle(file_name, specified_parent, parent_widget='toplevel'):
    from interface_tk import widget_model
    from view_tkinter import View
    import pickle
    view = View()
    view_model = [widget_model('root', specified_parent, parent_widget, 0, 0, 0, 0, 'nswe', **{})]
    with open(file_name, 'rb') as f:
        view_model += pickle.load(f)
    view.add_widgets(view_model)
    return view


class MyTestCase(unittest.TestCase):
    def test_list_of_balls(self):
        import GUI
        module = GUI.list_of_balls
        load_gui(module)

    def test_gui_create_card(self):
        import GUI
        module = GUI.create_card
        load_gui(module)

    def test_gui_sand_box(self):
        import GUI
        module = GUI.create_sand_box
        view = instantiate_view(module, width=250, height=100)
        # binding commands here - START

        # binding commands here - END
        view.launch_app()

    def test_save_sand_box_as_pickle(self):
        import GUI
        file_name = 'minutes_setter.gui'
        parent = 'minute_setter_parent'

        view_model = GUI.create_sand_box.get_view_model(parent)
        import pickle
        with open(file_name, 'wb') as f:
            pickle.dump(view_model, f)

    def test_load_pickle(self):
        file_name = 'minutes_setter.gui'
        specified_parent = 'minute_setter_parent'
        parent_widget = 'toplevel'

        app = load_gui_from_pickle(file_name, specified_parent, parent_widget)

        # binding commands here - START
        from Presenters.show_minute_setter import bind_command
        bind_command(app)
        # binding commands here - END

        app.launch_app()

    def test_gui_minutes_setter(self):
        import GUI
        module = GUI.minutes_setter
        view = instantiate_view(module, width=250, height=100)
        # binding commands here - START
        from Presenters.show_minute_setter import bind_command
        bind_command(view)
        # binding commands here - END
        view.launch_app()

    def test_combined_01(self):
        save_pickle = True

        import GUI
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()
        stacker.vstack(
            w.PanedWindow('pw_main', stacker).weights((1, 0)).is_vertical().stackers(
                w.Label('1').text(''),
                w.Label('2').text('')
            )
        )
        view_model = stacker.view_model
        view_model += GUI.list_of_balls.get_view_model('frame_1')
        view_model += GUI.create_card.get_view_model('frame_2')

        if save_pickle:
            import pickle
            with open('gui01.gui', 'wb') as f:
                pickle.dump(view_model, f)

        from view_tkinter import View
        view = View(width=800, height=900)
        view.add_widgets(view_model)
        view.launch_app()

    def test_combined_02(self):
        save_pickle = True
        import GUI
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()
        nb_frames = 'Cards', 'Detail'
        stacker.vstack(
            w.NoteBook('notebook_main', stacker).frame_names(nb_frames).stackers(
                w.Label('1').text(''),
                w.Label('2').text(''),
            )
        )
        view_model = stacker.view_model
        view_model += GUI.list_of_balls.get_view_model('frame_1')
        view_model += GUI.create_card.get_view_model('frame_2')

        if save_pickle:
            import pickle
            with open('gui02.gui', 'wb') as f:
                pickle.dump(view_model, f)

        from view_tkinter import View
        view = View(width=800, height=900)
        view.add_widgets(view_model)
        view.launch_app()


if __name__ == '__main__':
    unittest.main()
