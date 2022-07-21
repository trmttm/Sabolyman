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
        w.PanedWindow('paned_window_entry', stacker).is_horizontal().weights((3, 1)).stackers(
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
            w.Spacer(),
            w.Button(wn.button_delete_selected_actions).text('X').width(1),
            w.Button(wn.button_move_down_selected_actions).text('↓').width(1),
            w.Button(wn.button_move_up_selected_actions).text('↑').width(1),
            w.Button(wn.button_add_new_action).text('+').width(1),
            w.Spacer(),
        ),
        w.Spacer().adjust(-2),
    )


def get_actions_properties(stacker: Stacker):
    wn = WidgetNames
    return stacker.vstack(
        w.Label('lbl_actions_spacer'),
        stacker.hstack(
            w.Label('lbl_action_name').text('Name').width(10).padding(5, 0),
            w.Entry(wn.entry_action_name).default_value('Action Name', ).padding(25, 0),
            w.Label('lbl_action_deadline').text('Dead line:').width(10).padding(5, 0),
            w.Entry(wn.entry_action_dead_line).default_value('2022/07/22 15:00').padding(25, 0),
            w.Spacer().adjust(-3),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('lbl_owner').text('Owner').width(10).padding(5, 0),
            w.Entry(wn.entry_action_owner).default_value('Owner Name').padding(25, 0),
            w.Label('lbl_client').text('Client').width(10).padding(5, 0),
            w.Entry(wn.entry_action_client).default_value('Client Name').padding(25, 0),
            w.Spacer().adjust(-3),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('lbl_time').text('Time expected').width(10).padding(5, 0),
            w.Entry(wn.entry_action_time_expected).default_value('0:00').padding(25, 0),
            w.Label('lbl_done').text('Done').width(10).padding(5, 0),
            w.CheckButton(wn.check_button_action_done).value(False).padding(25, 0),
            w.Spacer().adjust(-3),
            w.Spacer().adjust(-2),
        ),
        w.NoteBook('notebook_actions', stacker).frame_names(('Detail', 'Files', 'Feedback')).stackers(
            w.TextBox(wn.text_box_action_description).padding(5, 5),
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
            w.Label(wn.label_card_dead_line).text('2022/5/30 15:00', ).padding(25, 0),
            w.Label('lbl_date_created1').text('Created:').width(6).padding(10, 0),
            w.Label(WidgetNames.label_date_created).text('2022/5/30 15:00').padding(10, 0),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label(wn.label_card_importance).text('Importance').width(10).padding(10, 0),
            w.Entry(wn.entry_card_importance).default_value(5).padding(25, 0).width(3),
            w.Spacer(),
        ),
        w.Spacer(),
    )
