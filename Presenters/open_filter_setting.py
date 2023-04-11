import Utilities
from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

specified_parent = 'popup_open_filter_setting'
ch_btn_finished = 'check_button_finished_cards'
ch_btn_filter_by_parent = 'check_button_filter_by_parent_card'
ch_btn_due_date = 'check_button_due_date'
entry_due_date = 'entry_due_date'
entry_search_box = 'entry_search_box'
combobox_search_mode = 'combobox_search_mode'
btn_clear_search = 'btn_clear_search'
ch_btn_priority = 'ch_btn_priority'
btn_priority_down = 'btn_priority_down'
btn_priority_up = 'btn_priority_up'
lbl_priority = 'lbl_priority'
priority = 5


def execute(v: ViewABC, commands: dict, states: dict):
    title = 'Filter setting'
    width = 550
    height = 200

    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]

    stacker = create_stacker(v, commands, states)
    view_model += stacker.view_model
    v.add_widgets(view_model)
    v.focus(entry_search_box)

    bind_commands_to_widgets(commands, states, v)


def create_stacker(v: ViewABC, commands: dict, states: dict) -> Stacker:
    stacker = Stacker(specified_parent)
    stacker.vstack(
        w.Label('blank_filter').text(''),
        stacker.hstack(
            w.Label('lbl_search_box').text('Search:').width(20).padding(20, 0),
            w.Entry(entry_search_box),
            w.ComboBox(combobox_search_mode).values(states['search_modes']).width(10),
            w.Button(btn_clear_search).text('x').width(1).padding(20, 0),
            w.Spacer().adjust(-3),
        ),
        stacker.hstack(
            w.Label('label_show_finished').text('Show Finished Cards').width(20).padding(20, 0),
            w.Spacer(),
            w.CheckButton(ch_btn_finished).value(states['show_finished']).padding(20, 0),
        ),
        stacker.hstack(
            w.Label('label_filter_by_parent').text('Filter by Parent Card').width(20).padding(20, 0),
            w.Spacer(),
            w.CheckButton(ch_btn_filter_by_parent).value(states['filter_by_parent']).padding(20, 0),
        ),
        stacker.hstack(
            w.Label('label_filter_by_due_date').text('Filter by due date').width(20).padding(20, 0),
            w.Entry(entry_due_date).width(20).default_value(states['due_date']),
            w.CheckButton(ch_btn_due_date).value(states['filter_by_date']).padding(20, 0),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label('label_filter_by_priority').text('Filter by priority').width(20).padding(20, 0),
            w.Button(btn_priority_down).text('▼').width(1),
            w.Label(lbl_priority).text(f'{priority}'),
            w.Button(btn_priority_up).text('▲').width(1),
            w.Spacer(),
            w.CheckButton(ch_btn_priority).value(states['filter_by_priority']).padding(20, 0),
        ),
        w.Spacer(),
        stacker.hstack(
            w.Button('btn_filter_default').text('Clear filters').command(
                lambda: clear_filters(commands, states, v)).padding(20, 5),
            w.Button('btn_filter_close').text('Done').command(lambda: v.close(specified_parent)).padding(20, 5),
            w.Spacer().adjust(-2),
            w.Spacer().adjust(-2),
        ),
    )
    return stacker


def bind_commands_to_widgets(commands: dict, states: dict, v):
    v.set_value(combobox_search_mode, states['search_modes'][0])
    v.bind_command_to_widget(ch_btn_finished, lambda: toggle_show_hide_finished_cards(v, commands))
    v.bind_command_to_widget(ch_btn_filter_by_parent, lambda: toggle_filter_by_parent(v, commands))
    v.bind_command_to_widget(ch_btn_due_date, lambda: toggle_due_date_filter(v, commands))
    v.bind_command_to_widget(entry_search_box, lambda *_: filter_by_search_word(commands, v))
    v.bind_command_to_widget(combobox_search_mode, lambda *_: filter_by_search_word(commands, v))
    v.bind_command_to_widget(btn_clear_search, lambda: commands['clear_search']())
    v.bind_command_to_widget(btn_priority_up, lambda: increment_priority(1, commands, states, v))
    v.bind_command_to_widget(btn_priority_down, lambda: increment_priority(-1, commands, states, v))
    v.bind_command_to_widget(ch_btn_priority, lambda: toggle_priority_filter(v, commands))
    v.bind_command_to_widget(specified_parent, lambda: close(v, commands))


def filter_by_search_word(commands: dict, v: ViewABC):
    commands['filter_with_keyword'](v.get_value(entry_search_box), v.get_value(combobox_search_mode))
    close(v, commands)


def toggle_show_hide_finished_cards(v: ViewABC, commands: dict):
    value: bool = v.get_value(ch_btn_finished)
    if value:
        commands['show_finished']()
    else:
        commands['hide_finished']()


def toggle_filter_by_parent(v: ViewABC, commands: dict):
    value: bool = v.get_value(ch_btn_filter_by_parent)
    if value:
        commands['filter_by_parent']()
    else:
        commands['clear_filter_by_parent']()


def toggle_due_date_filter(v: ViewABC, commands: dict):
    value: bool = v.get_value(ch_btn_due_date)
    if value:
        try:
            date = Utilities.str_to_date_time(v.get_value(entry_due_date)).date()
        except:
            date = None
        if date is not None:
            commands['filter_by_due_date'](date)
    else:
        commands['clear_filter_by_due_date']()


def toggle_priority_filter(v: ViewABC, commands: dict):
    value: bool = v.get_value(ch_btn_priority)
    if value:
        commands['filter_by_priority'](priority)
    else:
        commands['clear_filter_by_priority']()


def increment_priority(n: int, commands: dict, states: dict, v: ViewABC):
    global priority
    priority_max = states['priority_max']
    priority_min = states['priority_min']

    priority = max(min(priority + n, priority_max), priority_min)
    v.set_value(lbl_priority, priority)
    commands['reset_active_card']()


def clear_filters(commands: dict, states: dict, v: ViewABC):
    commands['clear_search']()
    v.set_value(ch_btn_finished, False)
    v.set_value(ch_btn_filter_by_parent, False)
    v.set_value(ch_btn_due_date, False)
    v.set_value(entry_due_date, states['due_date'])
    close(v, commands)


def close(v: ViewABC, commands: dict):
    v.close(specified_parent)
    commands['reset_active_card']()
