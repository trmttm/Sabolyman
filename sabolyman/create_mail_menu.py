from Interactor import InteractorABC


def execute(interactor: InteractorABC, path: str) -> dict:
    mail_template = {}
    mail_templates = {'Templates': mail_template}
    file_names = interactor.get_files_in_the_folder(path, 'txt')
    for file_name in file_names:
        mail_template.update({file_name: lambda f=file_name: interactor.create_email(f)})
    menu_injected = {
        'Mail': mail_templates,
    }
    return menu_injected
