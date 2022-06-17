from Entities import EntitiesABC
from Gateway import GatewayABC


def execute(e: EntitiesABC, g: GatewayABC, file_name: str, mail_template_package: str):
    text = g.read_text_file(file_name, mail_template_package)
    active_action = e.active_action
    name_receiver = active_action.owner.name

    replace = (('[name]', name_receiver),)
    for from_, to_ in replace:
        text = text.replace(from_, to_)

    return text
