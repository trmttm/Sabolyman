from stacker import Stacker
from stacker import widgets as w


def get_view_model(parent: str = 'root'):
    stacker = create_stacker(parent)
    view_model = stacker.view_model
    return view_model


def create_stacker(parent):
    stacker = Stacker(specified_parent=parent)
    stacker.vstack(
        stacker.hstack(
            w.Spacer(),
            w.Label('lbl_datetime_display').text('2023/1/1 17:00'),
            w.Spacer(),
        ),
        stacker.hstack(
            stacker.vstack(
                w.Button('btn_Y+').text('Y+').width(4),
                w.Button('btn_Y-').text('Y-').width(4),
                w.Spacer().adjust(-2),
                w.Spacer().adjust(-2),
            ),
            stacker.vstack(
                w.Button('btn_M+').text('M+').width(4),
                w.Button('btn_M-').text('M-').width(4),
                w.Spacer().adjust(-2),
                w.Spacer().adjust(-2),
            ),
            stacker.vstack(
                w.Button('btn_D+').text('D+').width(4),
                w.Button('btn_D-').text('D-').width(4),
                w.Spacer().adjust(-2),
                w.Spacer().adjust(-2),
            ),
            stacker.vstack(
                w.Button('btn_H+').text('H+').width(4),
                w.Button('btn_H-').text('H-').width(4),
                w.Spacer().adjust(-2),
                w.Spacer().adjust(-2),
            ),
            stacker.vstack(
                w.Button('btn_Min+').text('Min+').width(4),
                w.Button('btn_Min-').text('Min-').width(4),
                w.Spacer().adjust(-2),
                w.Spacer().adjust(-2),
            ),
            w.Spacer().adjust(-5),
            w.Spacer().adjust(-5),
            w.Spacer().adjust(-5),
            w.Spacer().adjust(-5),
            w.Spacer().adjust(-5),
        ),
        w.Spacer().adjust(-1),
        stacker.hstack(
            w.Button('btn_clear').text('Clear'),
            w.Button('btn_OK').text('OK'),
        ),
    )
    return stacker
