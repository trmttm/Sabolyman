import Utilities
import os_identifier
from Gateway.abc import GatewayABC


def open_folder(g: GatewayABC, uri: str):
    path = execute(g, uri)
    Utilities.open_file(path)


def execute(g: GatewayABC, uri: str) -> str:
    uri = g.adjust_uri_base(uri)
    if os_identifier.DIRECTORY_SEPARATOR in uri:
        split_by_slash = uri.split(os_identifier.DIRECTORY_SEPARATOR)
    else:
        split_by_slash = uri.split('/')
    last_element = split_by_slash[-1]
    if '.' not in last_element:
        folder_path = uri
    else:
        folder_path = uri.replace(last_element, '')
    return folder_path
