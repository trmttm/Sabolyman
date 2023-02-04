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


def bind_command_minutes_setter(view):
    import datetime
    d = datetime.timedelta()

    def clear_minutes():
        nonlocal d
        d = datetime.timedelta()
        update_label(d)

    def increment_minutes(minutes: int):
        nonlocal d
        d += datetime.timedelta(seconds=minutes * 60)
        update_label(d)

    def update_label(timedelta: datetime.timedelta):
        view.set_value('lbl_minutes', timedelta)

    def upon_ok(timedelta: datetime.timedelta):
        print(timedelta)

    view.bind_command_to_widget('btn_05', lambda: increment_minutes(5))
    view.bind_command_to_widget('btn_10', lambda: increment_minutes(10))
    view.bind_command_to_widget('btn_15', lambda: increment_minutes(15))
    view.bind_command_to_widget('btn_30', lambda: increment_minutes(30))
    view.bind_command_to_widget('btn_60', lambda: increment_minutes(60))
    view.bind_command_to_widget('btn_clear', lambda: clear_minutes())
    view.bind_command_to_widget('btn_OK', lambda: upon_ok(d))


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

    def test_gui_minutes_setter(self):
        import GUI
        module = GUI.minutes_setter
        view = instantiate_view(module, width=250, height=100)
        # binding commands here - START
        bind_command_minutes_setter(view)
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
        nb_frames = 'by Owners', 'Card Information'
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

    def test_load_pickle(self):
        from view_tkinter import View
        app = View()

        import pickle
        with open('gui02.gui', 'rb') as f:
            view_model = pickle.load(f)
        app.add_widgets(view_model)
        app.launch_app()


if __name__ == '__main__':
    unittest.main()
