from Gateway import GatewayABC


def execute(g: GatewayABC, file_name: str, mail_template_package: str) -> str:
    return g.read_text_file(file_name, mail_template_package)
