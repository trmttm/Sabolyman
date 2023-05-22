from typing import Callable

from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC

from . import show_email_creator


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, ask_folder: Callable, configure_menu: Callable,
            files_injected: tuple = ()):
    egp = e, g, p

    mail_template = {}
    mail_templates = {
        'Templates': mail_template,
        'Load more templates': lambda: load_email_templates(egp, execute, ask_folder, configure_menu, 'txt'),
    }

    file_names = g.get_files_in_the_folder(g.mail_template_path, 'txt')
    file_names += files_injected
    for file_name in sorted(file_names):
        mail_template.update({file_name: lambda f=file_name: show_email_creator.execute(egp, f)})

    menu_injected = {
        'Mail': mail_templates,
    }
    configure_menu(menu_injected)


def load_email_templates(epg: tuple, create_mail_menu: Callable, ask_folder: Callable, configure_menu: Callable,
                         specified_extension: str = ''):
    e: EntitiesABC = epg[0]
    g: GatewayABC = epg[1]
    p: PresentersABC = epg[2]

    folder_path = ask_folder()
    files = g.get_files_in_the_folder(folder_path, specified_extension)
    create_mail_menu(e, g, p, ask_folder, configure_menu, files)
