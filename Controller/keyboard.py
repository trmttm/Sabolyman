import os_identifier
from interface_keymaps import KeyMapsABC
from interface_view import ViewABC
from keyboard_shortcut import KeyMap

import WidgetNames as wn
from Entities import EntitiesABC
from Interactor import InteractorABC
from . import state
from . import utilities


def configure_keyboard_shortcut(app: ViewABC, i: InteractorABC, e: EntitiesABC):
    i.set_active_keymap('default')
    f = i.add_new_keyboard_shortcut

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

    def focus_cards_tree_then_actions_tree(active_card_is_my_ball, card_index, action_index):
        focus_on_tree_cards(active_card_is_my_ball, card_index)
        focus_on_tree_actions(action_index)

    def draw_node_graph_and_feedback():
        i.display_selected_card_as_a_graph_on_the_browser()
        kw = {'by_textbox': True, 'width': 800, 'height': 100}
        i.feed_back_user_by_popup('Graph drawn', f'{i.active_card.name} graph saved to {i.graph_folder_path}', **kw)

    def draw_node_graph_with_dynamic_config_and_feedback():
        i.display_selected_card_as_a_graph_on_the_browser_with_dynamic_config()
        kw = {'by_textbox': True, 'width': 800, 'height': 100}
        i.feed_back_user_by_popup('Graph drawn', f'{i.active_card.name} graph saved to {i.graph_folder_path}', **kw)

    def duplicate_and_feedback():
        message = f'Card {i.active_card.name} duplicated\n\n'
        i.duplicate_selected_card()
        kw = {'by_textbox': True, 'width': 800, 'height': 100}
        i.feed_back_user_by_popup('Cards duplicated', f'{message}', **kw)

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

    if os_identifier.is_mac:
        main_modifier = KeyMap.command
        sub_modifier = KeyMap.control
    else:
        main_modifier = KeyMap.control
        sub_modifier = KeyMap.control + KeyMap.shift

    f((main_modifier, KeyMap.l), (lambda: i.load_state_from_file(app.select_open_file(i.save_state_path)), ''))
    f((main_modifier, KeyMap.s), (lambda: i.save_state(), ''))
    f((main_modifier + KeyMap.shift, KeyMap.s), (lambda: i.save_to_file(utilities.default_file_path(i, e)), ''))
    f((main_modifier, KeyMap.w), (lambda: i.close(lambda: app.close('root')), ''))
    f((main_modifier, KeyMap.d), (lambda: duplicate_and_feedback(), ''))
    f((main_modifier, KeyMap.m), (lambda: i.make_email(), ''))
    f((main_modifier, KeyMap.zero), (lambda: i.open_display_progress_dialogue(), ''))
    f((main_modifier, KeyMap.nine), (lambda: i.open_display_new_tasks_dialogue(), ''))
    f((main_modifier, KeyMap.eight), (lambda: i.open_display_due_tasks_dialogue(), ''))

    f((main_modifier + KeyMap.shift, KeyMap.eight), (lambda: i.change_gui('gui01.gui'), ''))
    f((main_modifier + KeyMap.shift, KeyMap.nine), (lambda: i.change_gui('gui02.gui'), ''))
    f((main_modifier + KeyMap.shift, KeyMap.zero), (lambda: i.change_gui('gui03.gui'), ''))

    f((sub_modifier, KeyMap.c), (lambda: i.set_color_to_cards(state.get_left_tree_selected_indexes(app),
                                                              state.get_right_tree_selected_indexes(app),
                                                              app.ask_color()), ''))
    f((sub_modifier, KeyMap.h), (lambda: i.toggle_hide_finished_cards(), ''))
    f((main_modifier, KeyMap.f), (lambda: app.focus(wn.entry_search_box), ''))

    f((main_modifier, KeyMap.one), (lambda: i.sort_cards_by_color(), ''))
    f((main_modifier, KeyMap.two), (lambda: i.sort_cards_by_deadline(), ''))
    f((main_modifier, KeyMap.three), (lambda: i.sort_cards_by_name(), ''))
    f((main_modifier, KeyMap.four), (lambda: i.sort_cards_by_current_owner(), ''))
    f((main_modifier, KeyMap.five), (lambda: i.sort_by_importance(), ''))
    f((main_modifier, KeyMap.six), (lambda: i.sort_cards_by_current_client(), ''))

    f((main_modifier, KeyMap.i), (lambda: i.feed_back_user_by_popup('Implement?', 'Implement as a Card', height=100,
                                                                    action_ok=i.implement_lower_level_detail), ''))
    f((main_modifier, KeyMap.p), (lambda: draw_node_graph_and_feedback(), ''))
    f((main_modifier + KeyMap.shift, KeyMap.p), (lambda: draw_node_graph_with_dynamic_config_and_feedback(), ''))

    f((KeyMap.control, '-'), (lambda: i.shift_actions_dead_lines_by(-1, state.get_actions_selected_indexes(app)), ''))
    f((KeyMap.control, '='), (lambda: i.shift_actions_dead_lines_by(1, state.get_actions_selected_indexes(app)), ''))
    f((KeyMap.shift + KeyMap.control, '-'),
      (lambda: i.shift_actions_dead_lines_hours_by(-1, state.get_actions_selected_indexes(app)), ''))
    f((KeyMap.shift + KeyMap.control, '='),
      (lambda: i.shift_actions_dead_lines_hours_by(1, state.get_actions_selected_indexes(app)), ''))

    f((main_modifier, KeyMap.right), (lambda: i.jump_to_implementation_card(focus_cards_tree_then_actions_tree), ''))
    f((main_modifier, KeyMap.left), (lambda: i.jump_to_policy_action(focus_cards_tree_then_actions_tree), ''))
    f((main_modifier, KeyMap.j), (lambda: i.jump_to_card_list(focus_on_tree_cards), ''))
    f((main_modifier, KeyMap.k), (lambda: i.jump_to_action_list(focus_on_tree_actions), ''))
    f((main_modifier + KeyMap.shift, KeyMap.j), (lambda: toggle_focus_on_tree_cards(), ''))

    f((main_modifier + KeyMap.shift, KeyMap.c), (lambda: copy_and_feedback(), ''))
    f((main_modifier + KeyMap.shift, KeyMap.x), (lambda: cut_and_feedback(), ''))
    f((main_modifier + KeyMap.shift, KeyMap.v), (lambda: i.paste_actions_as_alias(), ''))

    f((main_modifier, KeyMap.e), (lambda: user_means_to_edit(), ''))

    # i.set_active_keymap('special')
    # f((KeyMap.command, KeyMap.a), (lambda: print('Hello!'), ''))
    # f((KeyMap.command, KeyMap.s), (lambda: i.set_active_keymap('default'), 'switched'))

    app.set_keyboard_shortcut_handler_to_root(lambda modifier, key: handler(i.keymaps, modifier, key))


def handler(k: KeyMapsABC, modifier, key):
    command, feedback = k.active_keymap.get_command_and_feedback((modifier, key))
    if command is not None:
        command()
