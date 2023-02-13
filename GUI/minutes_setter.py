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
            w.Label('lbl_minutes').text(f'00:00'),
        ),
        stacker.hstack(
            w.Button('btn_05').text('5').width(2),
            w.Button('btn_10').text('10').width(2),
            w.Button('btn_15').text('15').width(2),
            w.Button('btn_30').text('30').width(2),
            w.Button('btn_60').text('60').width(2),
        ),
        stacker.hstack(
            w.Button('btn_clear').text('Clear'),
            w.Button('btn_OK').text('OK'),
        ),
        w.Spacer().adjust(-2),
    )
    return stacker
