import gui
from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC

from Entities import EntitiesABC
from Interactor import InteractorABC
from . import keyboard_config_file
from . import utilities


def get_command_name_to_command(app: ViewABC, i: InteractorABC, e: EntitiesABC) -> dict:
    def duplicate_and_feedback():
        message = f'Card {i.active_card.name} duplicated\n\n'
        i.duplicate_selected_card()
        kw = {'by_textbox': True, 'width': 800, 'height': 100}
        i.feed_back_user_by_popup('Cards duplicated', f'{message}', **kw)

    return {
        'Load State from File': lambda: i.load_state_from_file(app.select_open_file(i.save_state_path)),
        'Save State': lambda: i.save_state(),
        'Save as new file': lambda: i.save_to_file(utilities.default_file_path(i, e)),
        'Save as...': lambda: i.save_to_file(
            app.select_save_file(initialdir=i.state_folder, initialfile=utilities.default_file_name(e))),
        'Close': lambda: i.close(lambda: app.close('root')),
        'Duplicate selected Card': lambda: duplicate_and_feedback(),
        'Draft Email': lambda: i.make_email(),
        'List of Progress': lambda: i.open_display_progress_dialogue(),
        'List of New Tasks': lambda: i.open_display_new_tasks_dialogue(),
        'List of Tasks due': lambda: i.open_display_due_tasks_dialogue(),

    }


specified_parent = 'pop_up_shortcut_setting'


def open_keyboard_shortcut_setting(v: ViewABC, i: InteractorABC, e: EntitiesABC, n_commands: int):
    v.add_widgets(_get_view_model_shortcut_setting(v, i, e, n_commands))
    [gui.bind_commands(n, v) for n in range(n_commands)]


def _get_view_model_shortcut_setting(v: ViewABC, i: InteractorABC, e: EntitiesABC, n_commands: int):
    title = 'Filter setting'
    width = 1000
    height = 500
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    commands_to_short_cuts = keyboard_config_file.get_method_name_to_key_combo(v, i, e)

    def callback(command_str):
        print(command_str, gui.get_state(v, n_commands))
        if command_str == gui.KEY_CANCEL:
            v.close(specified_parent)
        elif command_str == gui.KEY_APPLY:
            _save_commands(v, i, e)
        elif command_str == gui.KEY_DONE:
            _save_commands(v, i, e)
            v.close(specified_parent)

    return view_model + gui.create_view_model_of_shortcut_setter(callback, commands_to_short_cuts, specified_parent)


def _save_commands(v: ViewABC, i: InteractorABC, e: EntitiesABC):
    command_names = keyboard_config_file.get_method_name_to_key_combo(v, i, e).keys()
    file_path = keyboard_config_file.get_file_path(i)
    data = dict(zip(command_names, gui.get_state(v, len(command_names))))
    gui.save_shortcut_configuration_file(file_path, data)
    keyboard_config_file.configure_keyboard_shortcut(v, i, e)
