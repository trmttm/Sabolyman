from Gateway import GatewayABC
from Presenters import PresentersABC
from . import create_email_text


def execute(epg: tuple, file_name: str):
    g: GatewayABC = epg[1]
    p: PresentersABC = epg[2]

    file_names = g.get_files_in_the_folder(g.mail_template_path, 'txt')
    texts = tuple(create_email_text.execute(g, f, g.mail_template_package) for f in file_names)
    templates_to_text = dict(zip(file_names, texts))

    p.show_mail_creator(file_name, templates_to_text)
