from stacker import Stacker
from stacker import widgets as w


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
    return stacker.vstack(
        w.Label('lbl_actions').text('Actions'),
        w.TreeView('tree_actions'),
        w.Spacer().adjust(-1),
    )


def get_actions_properties(stacker: Stacker):
    return w.NoteBook('notebook_actions', stacker).frame_names(('i', 'Files', 'Feedback')).stackers(
        get_tab_one(stacker),
        w.TreeView('tree_action_files'),
        w.Label('lbl_notebook_3').text('3'),
    )


def get_card_property_entry(stacker: Stacker):
    return stacker.vstack(
        stacker.hstack(
            w.Label('lbl_name').text('Name').width(10),
            w.Entry('entry_name').default_value('New Card Name', ).padding(25, 0),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_dead_line').text('Deadline').width(10),
            w.Entry('entry_dead_line').default_value('2022/5/30', ).padding(25, 0),
            w.Spacer().adjust(-1),
        ),
        w.Spacer(),
    )


def get_tab_one(stacker: Stacker):
    return stacker.vstack(
        w.Label('lbl_description').text('Description').padding(5, 5),
        w.TextBox('text_description').padding(5, 5),
        stacker.hstack(
            w.Label('lbl_time').text('Time').width(10).padding(5, 5),
            w.Entry('entry_time').default_value('1:00').padding(5, 5),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_importance').text('Importance').width(10).padding(5, 5),
            w.Entry('entry_importance').default_value(5).padding(5, 5),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_done').text('Done').width(10).padding(5, 5),
            w.CheckButton('check_done').value(False).padding(5, 5),
            w.Spacer().adjust(-1),
        ),
        w.Spacer().adjust(-1),
    )
