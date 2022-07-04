from interface_view import ViewABC
from stacker import Stacker
from stacker import widgets as w
from view_tkinter.tk_interface import widget_model

specified_parent = 'popup_mail'
entry_recipient_name = 'entry_recipient_name'
text_box_mail_body_id = 'text_mail_body'
text_box_mail_id = 'text_mail'
combobox_templates_id = 'combo_box_template_picker'


def execute(v: ViewABC, template_name, template_to_text: dict):
    templates = tuple(template_to_text)
    text = template_to_text.get(template_name, '')

    view_model = create_view_model(templates)
    v.add_widgets(view_model)
    v.set_value(text_box_mail_id, text)
    v.set_value(combobox_templates_id, template_name)
    v.focus(combobox_templates_id)

    v.bind_command_to_widget(entry_recipient_name, lambda *_: update_text_mail(get_text(v, template_to_text), v))
    v.bind_command_to_widget(text_box_mail_body_id, lambda *_: update_text_mail(get_text(v, template_to_text), v))
    v.bind_command_to_widget(combobox_templates_id, lambda *_: update_text_mail(get_text(v, template_to_text), v))
    v.bind_command_to_widget(specified_parent, lambda: v.close(specified_parent))


def get_text(v: ViewABC, template_to_text: dict) -> str:
    key = v.get_value(combobox_templates_id)
    return template_to_text.get(key, '')


def create_view_model(templates: tuple):
    stacker = Stacker(specified_parent)
    stacker.vstack(
        w.ComboBox(combobox_templates_id).values(templates).padding(10, 0),
        w.Label('lbl_recipient').text('Recipient Name:').width(20).padding(10, 0),
        w.Entry(entry_recipient_name).default_value('RecipientName').padding(10, 0),
        w.Label('lbl_body').text('Body:').width(20).padding(10, 0),
        w.TextBox(text_box_mail_body_id).padding(10, 0),
        w.TextBox(text_box_mail_id).padding(10, 10),
    )
    view_model = [widget_model('root', specified_parent, 'toplevel', 0, 0, 0, 0, 'nswe', )]
    view_model += stacker.view_model
    return view_model


def update_text_mail(text: str, v: ViewABC):
    name_text = v.get_value(entry_recipient_name)
    body_text = v.get_value(text_box_mail_body_id)
    text = text.replace('[name]', name_text)
    if name_text == '各位':
        text = text.replace('さん', '')
        text = text.replace('様', '')
    text = text.replace('[body]', body_text)
    v.set_value(text_box_mail_id, text)
