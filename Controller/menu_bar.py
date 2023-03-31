import datetime
from os import path

import Utilities
from interface_view import ViewABC

import WidgetNames as wn
from Entities import EntitiesABC
from Interactor import InteractorABC
from . import state
from . import utilities


def configure_menu_bar(v: ViewABC, i: InteractorABC, e: EntitiesABC, menu_injected: dict = None):
    def focus_on_tree_actions(action_index: int = 0):
        v.focus(wn.tree_card_actions)
        v.select_multiple_tree_items(wn.tree_card_actions, (action_index,))

    menu_bar_model = {
        'File': {
            'Save Sate [cmd+s]': lambda: i.save_state(),
            'Save Sate as [shift+cmd+s]': lambda: i.save_to_file(
                v.select_save_file(initialdir=i.state_folder, initialfile=utilities.default_file_name(e))),
            'Load State': lambda: i.load_state_from_file(v.select_open_file(i.save_state_path)),
            'Select GUI': {
                'GUI 01': lambda: i.change_gui('gui01.gui'),
                'GUI 02': lambda: i.change_gui('gui02.gui'),
                'GUI 03': lambda: i.change_gui('gui03.gui'),
                'GUI 04': lambda: i.change_gui('gui04.gui'),
            },
        },
        'Export': {
            'Export Actions List': lambda: i.export_actions_list(
                v.select_save_file(i.home_folder, initialfile='Actions.csv'), ),
            'Export Gantt Chart': {
                'level 0': lambda: i.export_gantt_chart_data(),
                'level 1': lambda: i.export_gantt_chart_data(1),
                'level 2': lambda: i.export_gantt_chart_data(2),
                'level 3': lambda: i.export_gantt_chart_data(3),
                'level 4': lambda: i.export_gantt_chart_data(4),
            },
            'Display due tasks': lambda: i.open_display_due_tasks_dialogue(),
            'Display progress': lambda: i.open_display_progress_dialogue(),
            'Display new tasks': lambda: i.open_display_new_tasks_dialogue(),
            'Node Edge Graph': lambda: i.display_selected_card_as_a_graph_on_the_browser(),
            'Node Edge Graph (config)': lambda: i.display_selected_card_as_a_graph_on_the_browser_with_dynamic_config(),
        },
        'View': {
            'Open Filter Setting': i.open_filter_setting,
            'Clear All Filters': i.clear_all_filters,
            'Filter Finished Cards': {
                'Hide [ctrl+h]': i.hide_finished_cards,
                'Show [ctrl+h]': i.unhide_finished_cards,
            },
            'Filter by Due Date': {
                'Apply': lambda: i.filter_cards_by_due_date(),
                'Clear': lambda: i.clear_filter_due_date(),
            },
            'Filter by Parent Card': {
                'Apply': lambda: i.filter_cards_by_parent(),
                'Clear': lambda: i.clear_filter_by_parent(),
            },
        },
        'Cards': {
            'Jump ↑': lambda: i.jump_to_policy_action(focus_on_tree_actions),
            'Jump ↓': lambda: i.jump_to_implementation_card(focus_on_tree_actions),
            'Template Card': {
                'Load': lambda: i.load_template_card(v.select_open_file(i.cards_template_path)),
                'Save': lambda: i.save_as_template_card(v.select_save_file(i.cards_template_path)),
            },
            'Edit': {
                'Duplicate Card [cmd+d]': lambda: i.duplicate_selected_card(),
                'Set starting date to': lambda: i.reset_card_starting_date(state.get_left_tree_selected_indexes(v),
                                                                           state.get_right_tree_selected_indexes(v), ),
                'Set Color [ctrl+c]': lambda: i.set_color_to_cards(
                    state.get_left_tree_selected_indexes(v),
                    state.get_right_tree_selected_indexes(v),
                    v.ask_color()),
            },
            'Convert to Action(s)': lambda: i.convert_selected_cards_to_actions(state.get_trees_selected_indexes(v)),
            'Abstract out as an action': lambda: i.abstract_out_card_as_an_action_and_copy(),
            'Sort': {
                'By Color': i.sort_cards_by_color,
                'By Deadline': i.sort_cards_by_deadline,
                'By Name': i.sort_cards_by_name,
                'By Current Owner': i.sort_cards_by_current_owner,
                'By Current Client': i.sort_cards_by_current_client,
                'By Priority': i.sort_by_importance,
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
            'Cut': lambda: i.cut_actions(),
            'Paste as': {
                'Alias': lambda: i.paste_actions_as_alias(),
                'Duplicate copy': lambda: i.paste_actions_as_duplicate(),
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
    i.load_template_card(path.join(i.cards_template_path, file_name))
