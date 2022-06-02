from stacker import Stacker
from stacker import widgets as w


def get_view_model(parent: str = 'root'):
    stacker = Stacker(specified_parent=parent)
    stacker.vstack(
        stacker.hstack(
            list_of_balls('My Balls', 'my_balls', stacker),
            list_of_balls('Their Balls', 'their_balls', stacker),
            list_of_balls('Later', 'later', stacker),
            w.Spacer().adjust(-3),
            w.Spacer().adjust(-3),
            w.Spacer().adjust(-3),
        ),
    )

    view_model = stacker.view_model
    return view_model


def list_of_balls(text, name, stacker: Stacker):
    return stacker.vstack(
        w.Label(f'lbl_{name}').text(text).padding(5, 0),
        stacker.hstack(
            w.TreeView(f'tree_{name}').padding(5, 0),
        ),
        tree_buttons(name, stacker),
        w.Spacer().adjust(-2),
    )


def tree_buttons(name: str, stacker: Stacker):
    return stacker.hstack(
        w.Spacer(),
        w.Button(f'btn_{name}_delete').text('X').width(1),
        w.Button(f'btn_{name}_down').text('↓').width(1),
        w.Button(f'btn_{name}_up').text('↑').width(1),
        w.Button(f'btn_{name}_add').text('+').width(1),
        w.Spacer(),
    )
