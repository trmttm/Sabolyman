from stacker import Stacker
from stacker import widgets as w

import WidgetNames


def get_view_model(parent: str = 'root'):
    stacker = Stacker(specified_parent=parent)

    stacker.vstack(
        get_card_property_entry(stacker),
        get_actions(stacker),
        w.Spacer().adjust(-1),
    )

    view_model = stacker.view_model
    return view_model


def get_actions(stacker: Stacker):
    return stacker.hstack(
        w.PanedWindow('paned_window_entry', stacker).is_horizontal().stackers(
            get_actions_tree(stacker),
            get_actions_properties(stacker),
        ),
    )


def get_actions_tree(stacker: Stacker):
    wn = WidgetNames
    return stacker.vstack(
        w.Label('lbl_actions').text('Actions').padding(10, 0),
        stacker.hstack(
            w.TreeView(wn.tree_card_actions).padding(10, 10),
        ),
        stacker.hstack(
            w.Button('btn_remove_action').text('X').padding(0, 10),
            w.Button(wn.button_add_new_action).text('+').padding(0, 10),
            w.Button('btn_move_action_up').text('↑').padding(0, 10),
            w.Button('btn_move_action_down').text('↓').padding(0, 10),
            w.Spacer().adjust(-4),
            w.Spacer().adjust(-4),
            w.Spacer().adjust(-4),
            w.Spacer().adjust(-4),
        ),
        w.Spacer().adjust(-2),
    )


def get_actions_properties(stacker: Stacker):
    return stacker.vstack(
        w.Label('lbl_actions_spacer'),
        stacker.hstack(
            w.Label('lbl_action_name').text('Name').width(10).padding(5, 0),
            w.Entry('entry_action_name').default_value('Action Name', ).padding(25, 0).width(40),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_owner').text('Owner').width(10).padding(5, 0),
            w.Entry('entry_owner').default_value('Owner Name').padding(25, 0),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_time').text('Time expected').width(10).padding(5, 0),
            stacker.hstack(
                w.Entry('entry_time').default_value('1:00').padding(25, 0),
                w.Label('lbl_done').text('Done'),
                w.CheckButton('check_done').value(False).padding(25, 0),
                w.Spacer().adjust(-2),
            ),
            w.Spacer().adjust(-1),
        ),
        w.NoteBook('notebook_actions', stacker).frame_names(('Detail', 'Files', 'Feedback')).stackers(
            w.TextBox('text_description').padding(5, 5),
            stacker.vstack(
                w.TreeView('tree_action_files'),
            ),
            w.Label('lbl_notebook_3').text('3'),
        ),
        w.Spacer().adjust(-1)
    )


def get_card_property_entry(stacker: Stacker):
    wn = WidgetNames
    return stacker.vstack(
        stacker.hstack(
            w.Label('lbl_name').text('Name').width(10).padding(10, 0),
            w.Entry(wn.entry_card_name).default_value('New Card Name', ).padding(25, 0),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_dead_line').text('Deadline').width(10).padding(10, 0),
            w.Entry(wn.entry_dead_line).default_value('2022/5/30 15:00', ).padding(25, 0),
            w.Label('lbl_date_created1').text('Created: ').width(10).padding(10, 0),
            w.Label(WidgetNames.label_date_created).text('2022/5/28').width(10).padding(10, 0),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label(wn.label_card_importance).text('Importance').width(10).padding(10, 0),
            w.Entry(wn.entry_card_importance).default_value(5).padding(25, 0).width(20),
            w.Spacer(),
        ),
        w.Spacer(),
    )