import WidgetNames
from stacker import Stacker
from stacker import widgets as w

from .components.action_notes import ACTION_NOTES
from .components.action_properties import ACTION_PROPERTIES
from .components.action_resources import ACTION_RESOURCES


def get_view_model(parent: str = 'root', vertical: bool = False, **kwargs):
    stacker = create_stacker(parent, vertical, **kwargs)
    view_model = stacker.view_model
    return view_model


def create_stacker(parent, vertical: bool = False, **kwargs):
    stacker = Stacker(specified_parent=parent)
    stacker.vstack(
        get_card_property_entry(stacker),
        get_actions_vertical(stacker, **kwargs) if vertical else get_actions_horizontal(stacker, **kwargs),
        w.Spacer().adjust(-1),
    )
    return stacker


def get_actions_horizontal(stacker: Stacker, **kwargs):
    return stacker.hstack(
        w.PanedWindow('paned_window_entry', stacker).is_horizontal().weights((3, 1)).stackers(
            get_actions_tree(stacker),
            get_actions_properties(stacker, **kwargs),
        ),
    )


def get_actions_vertical(stacker: Stacker, **kwargs):
    return stacker.hstack(
        w.PanedWindow('paned_window_entry', stacker).is_vertical().weights((3, 1)).stackers(
            get_actions_tree(stacker),
            get_actions_properties(stacker, **kwargs),
        ),
    )


def get_actions_tree(stacker: Stacker, **kwargs):
    wn = WidgetNames
    return stacker.vstack(
        w.PanedWindow('pw_action_list_and_note', stacker).is_horizontal().stackers(
            w.TreeView(wn.tree_card_actions).padding(10, 10),
            ACTION_NOTES(wn),
        ),
        stacker.hstack(
            w.Spacer(),
            w.Button(wn.button_delete_selected_actions).text('X').width(1),
            w.Button(wn.button_move_down_selected_actions).text('↓').width(1),
            w.Button(wn.button_move_up_selected_actions).text('↑').width(1),
            w.Button(wn.button_add_new_action).text('+').width(1),
            w.Button(wn.button_display_resources).text('Resources'),
            w.Spacer(),
        ),
        w.Spacer().adjust(-2),
    )


def get_actions_properties(stacker: Stacker, **kwargs):
    wn = WidgetNames
    if kwargs.get('action_properties_by_paned_window'):
        return w.PanedWindow('pw_action_properties', stacker).is_horizontal().stackers(
            ACTION_PROPERTIES(stacker, wn),
            ACTION_RESOURCES(stacker),
        )
    else:
        return stacker.vstack(
            w.NoteBook(wn.notebook_actions, stacker).frame_names(('Properties', 'Notes', 'Resources')).stackers(
                ACTION_PROPERTIES(stacker, wn),
                ACTION_NOTES(wn),
                ACTION_RESOURCES(stacker),
            ),
            w.Spacer().adjust(-1)
        )


def get_card_property_entry(stacker: Stacker):
    wn = WidgetNames
    return stacker.vstack(
        stacker.hstack(
            w.Label('lbl_name').text('Card').width(10).padding(10, 0),
            w.Entry(wn.entry_card_name).default_value('New Card Name', ).padding(5, 0),
            w.Label(wn.label_card_importance).text('Priority').width(12).padding(10, 0),
            w.Button(wn.button_importance_down).text('-').width(1).padding(10, 0),
            w.Entry(wn.entry_card_importance).default_value(5).width(3),
            w.Button(wn.button_importance_up).text('+').width(1).padding(10, 0),
            w.Spacer().adjust(-5),
        ),
        stacker.hstack(
            w.Label('lbl_dead_line').text('Deadline').width(10).padding(10, 0),
            w.Label(wn.label_card_dead_line).text('2022/5/30 15:00', ).padding(5, 0),
            w.Label('lbl_date_created1').text('Created:').width(6).padding(0, 0),
            w.Label(WidgetNames.label_date_created).text('2022/5/30 15:00').padding(10, 0),
            w.Spacer(),
        ),
        stacker.hstack(
            w.Label('lbl_action_name').text('Action').width(10).padding(10, 0),
            w.Entry(wn.entry_action_name).default_value('Action Name', ).padding(10, 0),
            w.Spacer().adjust(-1),
        ),
        w.Spacer(),
    )
