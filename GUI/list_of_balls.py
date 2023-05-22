import WidgetNames
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
            list_of_balls('My Balls', 0, stacker),
            list_of_balls('Their Balls', 1, stacker),
            w.Spacer().adjust(-2),
            w.Spacer().adjust(-2),
        ),
        w.Spacer().adjust(-1),
    )
    return stacker


def list_of_balls(text, index, stacker: Stacker):
    wn = WidgetNames
    id_tree = wn.selector_tree_cards.get(index)

    return stacker.vstack(
        w.Label(f'lbl_cards_list_{index}').text(text).padding(5, 0),
        stacker.hstack(
            w.TreeView(id_tree).padding(5, 0),
        ),
        tree_buttons(index, stacker),
        w.Spacer().adjust(-2),
    )


def tree_buttons(index: int, stacker: Stacker):
    wn = WidgetNames
    id_del = wn.selector_button_delete_selected_card.get(index)
    id_down = wn.selector_button_move_down_selected_card.get(index)
    id_up = wn.selector_button_move_up_selected_card.get(index)
    id_add = wn.selector_button_add_card.get(index)
    id_insert = wn.selector_button_insert_card.get(index)

    return stacker.hstack(
        w.Spacer(),
        w.Button(id_del).text('X').width(1),
        w.Button(id_down).text('↓').width(1),
        w.Button(id_up).text('↑').width(1),
        w.Button(id_add).text('+').width(1),
        w.Button(id_insert).text('+i').width(2),
        w.Spacer(),
    )
