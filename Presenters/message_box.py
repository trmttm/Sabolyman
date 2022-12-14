from interface_tk import top_level_options
from interface_tk import widget_model
from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w

specified_parent = 'popup_mail'
button_id = 'pop_up_button_OK'
key_by_textbox = 'by_textbox'


def execute(v: ViewABC, title: str, body: str, width=400, height=200, **kwargs):
    stacker = Stacker(specified_parent)

    def select_text_widget():
        if by_textbox(kwargs):
            return w.TextBox('textbox_body').padding(10, 10)
        else:
            return w.Label('lbl_body').text(body).padding(10, 10).set_options('wraplength', width)

    stacker.vstack(
        select_text_widget(),
        w.Button(button_id).text('OK')
    )
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += stacker.view_model
    v.add_widgets(view_model)

    if by_textbox(kwargs):
        v.set_value('textbox_body', body)

    v.bind_command_to_widget(specified_parent, lambda: v.close(specified_parent))

    action_ok = kwargs.get('action_ok', None)
    if action_ok is None:
        v.bind_command_to_widget(button_id, lambda: v.close(specified_parent))
    else:
        v.bind_command_to_widget(button_id, lambda: upon_ok_button(action_ok, lambda: v.close(specified_parent)))

    v.focus(button_id)


def upon_ok_button(action_ok, close):
    action_ok(True)
    close()


def by_textbox(kwargs: dict) -> bool:
    return kwargs.get(key_by_textbox, None)
