from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w
from view_tkinter.tk_interface import top_level_options
from view_tkinter.tk_interface import widget_model

specified_parent = 'popup_mail'
button_id = 'pop_up_button_OK'


def execute(v: ViewABC, title: str, body: str, width=400, height=200, **kwargs):
    stacker = Stacker(specified_parent)
    stacker.vstack(
        w.Label('lbl_body').text(body).padding(10, 10).set_options('wraplength', width),
        w.Button(button_id).text('OK')
    )
    options = top_level_options(title, (width, height))
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', **options)]
    view_model += stacker.view_model
    v.add_widgets(view_model)

    v.bind_command_to_widget(specified_parent, lambda: v.close(specified_parent))
    action_ok = kwargs.get('action_ok', None)
    if action_ok is None:
        v.bind_command_to_widget(button_id, lambda: v.close(specified_parent))
    else:
        v.bind_command_to_widget(button_id, lambda :upon_ok_button(action_ok, lambda: v.close(specified_parent)))
    v.focus(button_id)


def upon_ok_button(action_ok, close):
    action_ok(True)
    close()
