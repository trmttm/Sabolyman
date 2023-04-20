from interface_view import ViewABC

from Entities import EntitiesABC
from Interactor import InteractorABC
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
