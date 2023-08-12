from stacker import widgets as w


def ACTION_PROPERTIES(stacker, wn):
    return stacker.vstack(
        stacker.hstack(
            w.Label('lbl_action_deadline').text('Dead line:').width(10).padding(5, 0),
            w.Entry(wn.entry_action_dead_line).default_value('2022/07/22 15:00').padding(25, 0),
            w.Button(wn.button_set_deadline).text('+').width(1).padding(25, 0),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('lbl_action_start').text('Start from:').width(10).padding(5, 0),
            w.Entry(wn.entry_action_start_from).default_value('2022/07/22 15:00').padding(25, 0),
            w.Button(wn.button_set_start_from).text('+').width(1).padding(25, 0),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('lbl_owner').text('Owner').width(10).padding(5, 0),
            w.Entry(wn.entry_action_owner).default_value('Owner Name').padding(25, 0),
            w.Button(wn.button_set_owner).text('+').width(1).padding(25, 0),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('lbl_client').text('Client').width(10).padding(5, 0),
            w.Entry(wn.entry_action_client).default_value('Client Name').padding(25, 0),
            w.Button(wn.button_set_client).text('+').width(1).padding(25, 0),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('lbl_time').text('Time expected').width(10).padding(5, 0),
            stacker.hstack(
                w.Entry(wn.entry_action_time_expected).default_value('0:00').padding(25, 0).width(10),
                w.Button(wn.button_set_duration).text('+').width(1).padding(25, 0),
            ),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_scheduled').text('Scheduled').width(10).padding(5, 0),
            w.CheckButton(wn.check_button_action_scheduled).value(False).padding(25, 0),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('lbl_done').text('Done').width(10).padding(5, 0),
            w.CheckButton(wn.check_button_action_done).value(False).padding(25, 0),
            w.Spacer().adjust(-2),
        ),
        w.Spacer(),
    )
