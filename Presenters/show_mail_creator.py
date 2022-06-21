from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w
from view_tkinter.tk_interface import widget_model

specified_parent = 'popup_mail'
entry_recipient_name = 'entry_recipient_name'
text_box_mail_body_id = 'text_mail_body'
text_box_mail_id = 'text_mail'


def execute(v: ViewABC, text: str):
    view_model = create_view_model()
    v.add_widgets(view_model)
    v.set_value(text_box_mail_id, text)
    v.bind_command_to_widget(entry_recipient_name, lambda *_: update_text_mail(text, v))
    v.bind_command_to_widget(text_box_mail_body_id, lambda *_: update_text_mail(text, v))
    v.bind_command_to_widget(specified_parent, lambda: v.close(specified_parent))


def create_view_model():
    stacker = Stacker(specified_parent)
    stacker.vstack(
        w.Label('lbl_recipient').text('Recipient Name:'),
        w.Entry(entry_recipient_name).default_value('RecipientName'),
        w.Label('lbl_body').text('Body:'),
        w.TextBox(text_box_mail_body_id).padding(10, 10),
        w.TextBox(text_box_mail_id).padding(10, 10),
    )
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', )]
    view_model += stacker.view_model
    return view_model


def update_text_mail(text: str, v: ViewABC):
    name_text = v.get_value(entry_recipient_name)
    body_text = v.get_value(text_box_mail_body_id)
    text = text.replace('[name]', name_text)
    text = text.replace('[body]', body_text)
    v.set_value(text_box_mail_id, text)
