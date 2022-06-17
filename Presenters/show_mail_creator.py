from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w
from view_tkinter.tk_interface import widget_model

specified_parent = 'popup_mail'
text_box_mail_body_id = 'text_mail_body'
text_box_mail_id = 'text_mail'


def execute(v: ViewABC, text: str):
    view_model = create_view_model()
    v.add_widgets(view_model)
    v.bind_command_to_widget(text_box_mail_body_id, lambda *_: update_text_mail(text, v))


def create_view_model():
    stacker = Stacker(specified_parent)
    stacker.vstack(
        w.Label('lbl_body').text('Body:'),
        w.TextBox(text_box_mail_body_id).padding(10, 10),
        w.TextBox(text_box_mail_id).padding(10, 10),
    )
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', )]
    view_model += stacker.view_model
    return view_model


def update_text_mail(current_text: str, v: ViewABC):
    body_text = v.get_value(text_box_mail_body_id)
    text = current_text.replace('[body]', body_text)
    v.set_value(text_box_mail_id, text)
