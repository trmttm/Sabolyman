from GUI.list_of_actions import constants as c
from stacker import Stacker
from stacker import widgets as w


def SCROLLABLE(data: dict, stacker: Stacker):
    return stacker.vstack_scrollable(
        *ALL_CARDS_WIDGETS(stacker, data)
    )


def TITLE_LABEL(stacker: Stacker):
    return stacker.hstack(
        w.Spacer(),
        w.Label(c.LABEL_TITLE).text('Title').padding(0, 20),
        w.Spacer(),
    )


def BUTTOM_BUTTONS(stacker: Stacker):
    return stacker.hstack(
        w.Spacer(),
        w.Button(c.BTN_ACTIONS_CANCEL).text('Cancel').padding(5, 10),
        w.Button(c.BTN_REPLACE).text('Replace').padding(5, 10),
        w.Button(c.BTN_ACTIONS_REVERT_ALL).text('Revert All').padding(5, 10),
        w.Button(c.BTN_ACTIONS_APPLY).text('Apply').padding(5, 10),
        w.Button(c.BTN_ACTIONS_OK).text('Done').padding(5, 10),
        w.Spacer(),
    )


def ALL_CARDS_WIDGETS(stacker, data: dict) -> tuple:
    card_widgets = ()
    for n, card_state in enumerate(data[c.KEY_CARD_STATES]):
        card_widgets += CARD_WIDGETS(stacker, n, data)
    return card_widgets


def CARD_WIDGETS(stacker, n: int, data: dict):
    return (
        w.Label('blank').text(''),
        w.Label(f'card_name_{n}').text(data[c.KEY_CARD_STATES][n][c.CARD_NAME]).padding(c.CARD_PADX, 0),

    ) + ACTION_WITHIN_A_CARD(stacker, data[c.KEY_CARD_STATES][n])


def ACTION_WITHIN_A_CARD(stacker, action_state):
    return tuple(
        stacker.hstack(
            w.Label(f'{c.ACTION_NAME}{action_id}').text(action_state.get(c.KEY_NAMES, ())[n]).padding(c.ACTION_PADX, 0),
            w.Entry(f'{c.OWNER}{action_id}').default_value(f'{owner}'),
            w.Button(f'{c.BTN_DD_DOWN}{action_id}').text('↓').width(2),
            w.Entry(f'{c.ENTRY_DD}{action_id}').default_value(action_state.get(c.KEY_DUE_DATES, ())[n]),
            w.Button(f'{c.BTN_DD_UP}{action_id}').text('↑').width(2),
            w.Label(f'label_done{action_id}').text('D').width(2),
            w.CheckButton(f'{c.CB_DONE}{action_id}').value(action_state.get(c.KEY_DONE_OR_NOT, ())[n]),
            w.Label(f'label_scheduled{action_id}').text('S').width(2),
            w.CheckButton(f'{c.CB_SCHEDULED}{action_id}').value(action_state.get(c.KEY_SCHEDULED, ())[n]),
            w.Entry(f'{c.ENTRY_DURATION}{action_id}').default_value(action_state.get(c.KEY_DURATION, ())[n]).width(10),
            w.Button(f'{c.BTN_SET_DURATION}{action_id}').text('+').width(2),
            w.Button(f'{c.BTN_REVERT}{action_id}').text('↩︎').width(2),
            w.Spacer().adjust(-12),
        ) for (n, (action_id, owner)) in
        enumerate(zip(action_state.get(c.KEY_ACTION_IDS, ()), action_state.get(c.KEY_OWNERS, ()), ))
    )
