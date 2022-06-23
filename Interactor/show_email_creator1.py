from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC
from . import show_email_creator


def execute(e: EntitiesABC, p: PresentersABC, g: GatewayABC):
    file_names = g.get_files_in_the_folder(g.mail_template_path, 'txt')
    if len(file_names) > 0:
        file_name = file_names[0]
        show_email_creator.execute((e, g, p), file_name)
