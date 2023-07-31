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


def create_data() -> dict:
    import datetime
    import Utilities
    import GUI.list_of_actions.constants as c
    data = {
        c.KEY_DATE: datetime.datetime(2023, 5, 15),
        c.KEY_CARD_STATES: (
            {
                c.CARD_NAME: 'Card 01',
                c.KEY_ACTION_IDS: (
                    'id0101',
                    'id0102',
                    'id0103',
                    'id0104',
                ),
                c.KEY_NAMES: (
                    'action 0101',
                    'action 0102',
                    'action 0103',
                    'action 0104',
                ),
                c.KEY_DONE_OR_NOT: (
                    False,
                    False,
                    False,
                    False,
                ),
                c.KEY_DUE_DATES: (
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/12')),
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/13')),
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/14')),
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/15')),
                ),
            },
            {
                c.CARD_NAME: 'Card 02',
                c.KEY_ACTION_IDS: (
                    'id0201',
                    'id0202',
                    'id0203',
                    'id0204',
                ),
                c.KEY_NAMES: (
                    'action 0201',
                    'action 0202',
                    'action 0203',
                    'action 0204',
                ),
                c.KEY_DONE_OR_NOT: (
                    False,
                    False,
                    False,
                    False,
                ),
                c.KEY_DUE_DATES: (
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/15')),
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/15')),
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/15')),
                    Utilities.datetime_to_str_no_time(Utilities.str_to_date_time_no_time('2023/5/15')),
                ),
            },
        )
    }
    return data


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

        view_model = GUI.minutes_setter.get_view_model(parent)
        import pickle
        with open(file_name, 'wb') as f:
            pickle.dump(view_model, f)

    def test_load_pickle(self):
        file_name = 'datetime_setter.gui'
        specified_parent = 'datetime_setter_parent'
        parent_widget = 'toplevel'

        app = load_gui_from_pickle(file_name, specified_parent, parent_widget)

        # binding commands here - START
        from Presenters.show_datetime_setter import bind_command
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

    def test_datetime_setter(self):
        import GUI
        module = GUI.datetime_setter
        view = instantiate_view(module, width=400, height=150)
        # binding commands here - START
        from Presenters.show_datetime_setter import bind_command
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

    def test_combined_03(self):
        save_pickle = True

        import GUI
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()
        stacker.vstack(
            w.PanedWindow('pw_main', stacker).weights((1, 0)).is_horizontal().stackers(
                w.Label('1').text(''),
                w.Label('2').text('')
            )
        )
        view_model = stacker.view_model
        view_model += GUI.list_of_balls.get_view_model('frame_1')
        view_model += GUI.create_card.get_view_model('frame_2')

        if save_pickle:
            import pickle
            with open('gui03.gui', 'wb') as f:
                pickle.dump(view_model, f)

        from view_tkinter import View
        view = View(fullscreen=True)
        view.add_widgets(view_model)
        view.launch_app()

    def test_combined_04(self):
        save_pickle = True

        import GUI
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()
        stacker.vstack(
            w.PanedWindow('pw_main', stacker).weights((1, 0)).is_horizontal().stackers(
                w.Label('1').text(''),
                w.Label('2').text('')
            )
        )
        view_model = stacker.view_model
        view_model += GUI.list_of_balls.get_view_model('frame_1')
        view_model += GUI.create_card.get_view_model('frame_2', vertical=True)

        if save_pickle:
            import pickle
            with open('gui04.gui', 'wb') as f:
                pickle.dump(view_model, f)

        from view_tkinter import View
        view = View(fullscreen=True)
        view.add_widgets(view_model)
        view.launch_app()

    def test_list_of_actions(self):

        from view_tkinter import View
        view = View()

        from Presenters.open_display_list_of_actions import pop_up_list_of_actions
        data = create_data()

        def callback(state: tuple):
            print()
            for action_state in state:
                print(action_state)

        pop_up_list_of_actions(data, view, callback)
        view.launch_app()

    def test_list_of_resources(self):
        from view_tkinter import View
        view = View()

        from Presenters import open_list_of_resources
        cards = ('Card01', 'Card02', 'Card03', 'Card04', 'Card05',)
        actions = ('Action01', 'Action02', 'Action03', 'Action04', 'Action05',)
        resources = ('File Name 01', 'File Name 02', 'File Name 03', 'File Name 04', 'File Name 05',)
        extensions = ('Ext01', 'Ext02', 'Ext03', 'Ext04', 'Ext05',)
        paths = ('Path01', 'Path02', 'Path03', 'Path04', 'Path05',)
        data = cards, actions, resources, extensions, paths

        from GUI.list_of_recources import constants as c
        commands = {
            c.CMD_OPEN_FILE: lambda *args: print('Open file', args),
            c.CMD_OPEN_FOLDER: lambda *args: print('Open folder', args),
        }
        open_list_of_resources.execute(view, data, commands)
        view.launch_app()


if __name__ == '__main__':
    unittest.main()
