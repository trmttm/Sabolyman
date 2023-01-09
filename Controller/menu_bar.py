import datetime
from os import path

import Utilities
from interface_view import ViewABC

from Entities import EntitiesABC
from Interactor import InteractorABC
from . import state
from . import utilities


def configure_menu_bar(v: ViewABC, i: InteractorABC, e: EntitiesABC, menu_injected: dict = None):
    menu_bar_model = {
        'File': {
            'Save Sate [cmd+s]': lambda: i.save_state(),
            'Save Sate as [shift+cmd+s]': lambda: i.save_to_file(
                v.select_save_file(initialfile=utilities.default_file_name(e))),
            'Load State': lambda: i.load_state_from_file(v.select_open_file()),
        },
        'Export': {
            'Export Actions List': lambda: i.export_actions_list(
                v.select_save_file(i.home_folder, initialfile='Actions.csv'), ),
            'Display due tasks': lambda: i.open_display_due_tasks_dialogue(),
            'Display progress': lambda: i.open_display_progress_dialogue(),
            'Display new tasks': lambda: i.open_display_new_tasks_dialogue(),
        },
        'View': {
            'Hide Finished Cards [ctrl+h]': i.hide_finished_cards,
            'Show Finished Cards [ctrl+h]': i.unhide_finished_cards,
        },
        'Cards': {
            'Set starting date to': lambda: i.reset_card_starting_date(state.get_left_tree_selected_indexes(v),
                                                                       state.get_right_tree_selected_indexes(v), ),
            'Save as Template Card': lambda: i.save_as_template_card(v.select_save_file()),
            'Add Template Card': lambda: i.add_template_card(v.select_open_file()),
            'Duplicate Card [cmd+d]': lambda: i.duplicate_selected_card(),
            'Set Color [ctrl+c]': lambda: i.set_color_to_cards(
                state.get_left_tree_selected_indexes(v),
                state.get_right_tree_selected_indexes(v),
                v.ask_color()),
            'Convert to Action(s)': lambda: i.convert_selected_cards_to_actions(state.get_trees_selected_indexes(v)),
            'Sort': {
                'By Color': i.sort_cards_by_color,
                'By Deadline': i.sort_cards_by_deadline,
                'By Name': i.sort_cards_by_name,
                'By Current Owner': i.sort_cards_by_current_owner,
                'By Current Client': i.sort_cards_by_current_client,
            },
            'Shift Deadlines by': {
                '+5 day': lambda: i.shift_cards_dead_lines_by(5,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '+4 day': lambda: i.shift_cards_dead_lines_by(4,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '+3 day': lambda: i.shift_cards_dead_lines_by(3,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '+2 day': lambda: i.shift_cards_dead_lines_by(2,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '+1 day': lambda: i.shift_cards_dead_lines_by(1,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '-1 day': lambda: i.shift_cards_dead_lines_by(-1,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '-2 day': lambda: i.shift_cards_dead_lines_by(-2,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '-3 day': lambda: i.shift_cards_dead_lines_by(-3,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '-4 day': lambda: i.shift_cards_dead_lines_by(-4,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
                '-5 day': lambda: i.shift_cards_dead_lines_by(-5,
                                                              state.get_left_tree_selected_indexes(v),
                                                              state.get_right_tree_selected_indexes(v), ),
            },
        },
        'Actions': {
            'Copy': lambda: i.copy_actions(),
            'Paste as': {
                'Duplicate copy': lambda: i.paste_actions_as_duplicate(),
                'Alias': lambda: i.paste_actions_as_alias(),
            },
            'Set Color': lambda: i.set_color_to_actions(
                state.get_actions_selected_indexes(v),
                v.ask_color()),
            'Implement lower level detail': lambda: i.implement_lower_level_detail(),
        },
        'Habits': {
            'Morning': lambda: load_habit(i, 'Habit - Wake up.card'),
            'Work Beginning': lambda: load_habit(i, 'Habit - Beginning of Work.card'),
            'Work End': lambda: load_habit(i, 'Habit - End of Work.card'),
            'Evening': lambda: load_habit(i, 'Habit - Evening.card'),
        },
    }
    if menu_injected is not None:
        menu_bar_model.update(menu_injected)
    v.update_menu_bar(menu_bar_model)


def now() -> str:
    f = Utilities.get_two_digit_str_from_int
    now = datetime.datetime.now()
    month = f(now.month)
    day = f(now.day)
    hour = f(now.hour)
    minute = f(now.minute)
    return f'{now.year}{month}{day}_{hour}{minute}'


def load_habit(i: InteractorABC, file_name: str):
    i.add_template_card(path.join(i.cards_template_path, file_name))
