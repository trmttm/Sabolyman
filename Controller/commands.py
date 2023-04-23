import shortcut_setter as ss
from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC

import WidgetNames as wn
from Entities.abc_entities import EntitiesABC
from Interactor.abc import InteractorABC
from . import keyboard_config_file
from . import state
from . import utilities


def get_command_name_to_command(app: ViewABC, i: InteractorABC, e: EntitiesABC) -> dict:
    def focus_on_tree_actions(action_index: int = 0):
        app.focus(wn.tree_card_actions)
        app.select_multiple_tree_items(wn.tree_card_actions, (action_index,))

    def toggle_focus_on_tree_cards():
        tree_id = wn.tree_my_cards if not i.active_card_in_my_ball else wn.tree_their_cards
        app.focus(tree_id)
        app.select_multiple_tree_items(tree_id, (i.active_card_index,))

    def focus_on_tree_cards(active_card_is_my_ball: bool, card_index):
        tree_id = wn.tree_my_cards if active_card_is_my_ball else wn.tree_their_cards
        app.focus(tree_id)
        app.select_multiple_tree_items(tree_id, (card_index,))

    def duplicate_and_feedback():
        message = f'Card {i.active_card.name} duplicated\n\n'
        i.duplicate_selected_card()
        kw = {'by_textbox': True, 'width': 800, 'height': 100}
        i.feed_back_user_by_popup('Cards duplicated', f'{message}', **kw)

    def draw_node_graph_and_feedback():
        i.display_selected_card_as_a_graph_on_the_browser()
        kw = {'by_textbox': True, 'width': 800, 'height': 100}
        i.feed_back_user_by_popup('Graph drawn', f'{i.active_card.name} graph saved to {i.graph_folder_path}', **kw)

    def draw_node_graph_with_dynamic_config_and_feedback():
        i.display_selected_card_as_a_graph_on_the_browser_with_dynamic_config()
        kw = {'by_textbox': True, 'width': 800, 'height': 100}
        i.feed_back_user_by_popup('Graph drawn', f'{i.active_card.name} graph saved to {i.graph_folder_path}', **kw)

    def focus_cards_tree_then_actions_tree(active_card_is_my_ball, card_index, action_index):
        focus_on_tree_cards(active_card_is_my_ball, card_index)
        focus_on_tree_actions(action_index)

    def copy_and_feedback():
        i.copy_actions()
        message = 'Action(s) copied\n\n'
        for n, a in enumerate(i.copied_actions):
            message += f'{n + 1}:  {a.name}\n'
        kw = {'by_textbox': True, 'width': 800, 'height': 200}
        i.feed_back_user_by_popup('Actions copied', f'{message}', **kw)

    def cut_and_feedback():
        i.cut_actions()
        message = 'Action(s) cut\n\n'
        for n, a in enumerate(i.copied_actions):
            message += f'{n + 1}:  {a.name}\n'
        kw = {'by_textbox': True, 'width': 800, 'height': 200}
        i.feed_back_user_by_popup('Actions cut', f'{message}', **kw)

    def user_means_to_edit():
        print('User means to edit')
        i.reset_recursive_counter()

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
        'Change to GUI01': lambda: i.change_gui('gui01.gui'),
        'Change to GUI02': lambda: i.change_gui('gui02.gui'),
        'Change to GUI03': lambda: i.change_gui('gui03.gui'),
        'Change to GUI04': lambda: i.change_gui('gui04.gui'),
        'Open Card Color Picker': lambda: i.set_color_to_cards(state.get_left_tree_selected_indexes(app),
                                                               state.get_right_tree_selected_indexes(app),
                                                               app.ask_color()),
        'Open Action Color Picker': lambda: i.set_color_to_actions(state.get_actions_selected_indexes(app),
                                                                   app.ask_color()),
        'Toggle Hide Finished Cards': lambda: i.toggle_hide_finished_cards(),
        'Open Filter Setting': lambda: i.open_filter_setting(),
        'Sort Cards by color': lambda: i.sort_cards_by_color(),
        'Sort Cards by deadline': lambda: i.sort_cards_by_deadline(),
        'Sort Cards by name': lambda: i.sort_cards_by_name(),
        'Sort Cards by current owner': lambda: i.sort_cards_by_current_owner(),
        'Sort Cards by importance': lambda: i.sort_by_importance(),
        'Sort Cards by current client': lambda: i.sort_cards_by_current_client(),

        'Implement Action': lambda: i.feed_back_user_by_popup('Implement?', 'Implement as a Card', height=100,
                                                              action_ok=i.implement_lower_level_detail),
        'Draw Node and feedback': lambda: draw_node_graph_and_feedback(),
        'Draw Node with dynamic configuration and feedback': lambda: draw_node_graph_with_dynamic_config_and_feedback(),

        'Action deadline -1 Day': lambda: i.shift_actions_dead_lines_by(-1, state.get_actions_selected_indexes(app)),
        'Action deadline +1 Day': lambda: i.shift_actions_dead_lines_by(1, state.get_actions_selected_indexes(app)),
        'Action deadline -1 Hour': lambda: i.shift_actions_dead_lines_hours_by(-1,
                                                                               state.get_actions_selected_indexes(app)),
        'Action deadline +1 Hour': lambda: i.shift_actions_dead_lines_hours_by(1,
                                                                               state.get_actions_selected_indexes(app)),

        'Jump to Implementation Card': lambda: i.jump_to_implementation_card(focus_cards_tree_then_actions_tree),
        'Jump to Policy Action': lambda: i.jump_to_policy_action(focus_cards_tree_then_actions_tree),
        'Focus on Tree Cards': lambda: i.jump_to_card_list(focus_on_tree_cards),
        'Focus on Tree Actions': lambda: i.jump_to_action_list(focus_on_tree_actions),
        'Switch focus between my vs their balls': lambda: toggle_focus_on_tree_cards(),
        'Copy selected actions': lambda: copy_and_feedback(),
        'Cut selected actions': lambda: cut_and_feedback(),
        'Paste actions as alias': lambda: i.paste_actions_as_alias(),
        'Paste actions as duplicate copy': lambda: i.paste_actions_as_duplicate(),
        'Filter by parent': lambda: i.filter_cards_by_parent(),
        'Filter move up on parent': lambda: i.filter_move_up_one_parent(),
        'Clear all filters': lambda: i.clear_all_filters(),
        'Apply filter by due date': lambda: i.filter_cards_by_due_date(),
        'Clear filter by due date': lambda: i.clear_filter_due_date(),
        'User means to edit': lambda: user_means_to_edit(),

        'Export Actions List': lambda: i.export_actions_list(
            app.select_save_file(i.home_folder, initialfile='Actions.csv'), ),
        'Export Gantt Chart level 0': lambda: i.export_gantt_chart_data(),
        'Export Gantt Chart level 1': lambda: i.export_gantt_chart_data(1),
        'Export Gantt Chart level 2': lambda: i.export_gantt_chart_data(2),
        'Export Gantt Chart level 3': lambda: i.export_gantt_chart_data(3),
        'Export Gantt Chart level 4': lambda: i.export_gantt_chart_data(4),

        'Load Template card': lambda: i.add_new_card(),
        'Save as Template card': lambda: i.save_as_template_card(app.select_save_file(i.cards_template_path)),

        'Abstract out as an action': lambda: i.abstract_out_card_as_an_action_and_copy(
            state.get_left_tree_selected_indexes(app),
            state.get_right_tree_selected_indexes(app),
        ),

        'Display Action Properties': lambda: app.select_note_book_tab(wn.notebook_actions, 0),
        'Display Action Notes': lambda: app.select_note_book_tab(wn.notebook_actions, 1),
        'Display Action Resources': lambda: app.select_note_book_tab(wn.notebook_actions, 2),

    }


specified_parent = 'pop_up_shortcut_setting'


def open_keyboard_shortcut_setting(v: ViewABC, i: InteractorABC, e: EntitiesABC):
    command_names = keyboard_config_file.get_method_name_to_key_combo(v, i, e).keys()
    n_commands = len(command_names)
    v.add_widgets(_get_view_model_shortcut_setting(v, i, e, n_commands))
    [ss.bind_commands(n, v) for n in range(n_commands)]


def _get_view_model_shortcut_setting(v: ViewABC, i: InteractorABC, e: EntitiesABC, n_commands: int):
    title = 'Filter setting'
    width = 1000
    height = 500
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    commands_to_short_cuts = keyboard_config_file.get_method_name_to_key_combo(v, i, e)

    def callback(command_str):
        print(command_str, ss.get_state(v, n_commands))
        if command_str == ss.KEY_CANCEL:
            v.close(specified_parent)
        elif command_str == ss.KEY_APPLY:
            _save_commands(v, i, e)
        elif command_str == ss.KEY_DONE:
            _save_commands(v, i, e)
            v.close(specified_parent)

    return view_model + ss.create_view_model_of_shortcut_setter(callback, commands_to_short_cuts, specified_parent)


def _save_commands(v: ViewABC, i: InteractorABC, e: EntitiesABC):
    command_names = keyboard_config_file.get_method_name_to_key_combo(v, i, e).keys()
    file_path = keyboard_config_file.get_file_path(i)
    data = dict(zip(command_names, ss.get_state(v, len(command_names))))
    ss.save_shortcut_configuration_file(file_path, data)
    keyboard_config_file.configure_keyboard_shortcut(v, i, e)
