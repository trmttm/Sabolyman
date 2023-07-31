from Entities import Action
from Entities import Card
from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from GUI.list_of_recources import constants as c
from Gateway.abc import GatewayABC
from Presenters import PresentersABC

from .convert_uri_to_folder_path import open_file
from .convert_uri_to_folder_path import open_folder


def execute(e: EntitiesABC, p: PresentersABC, g: GatewayABC):
    s: SynchronizerABC = e.synchronizer
    action = e.active_action
    commands = {
        c.CMD_OPEN_FILE: lambda uri: open_file(g, uri),
        c.CMD_OPEN_FOLDER: lambda uri: open_folder(g, uri)
    }
    if action is not None:
        resource_datas = {}
        gather_resources_datas_recursively(e.active_card, action, s, resource_datas)
        data = adapter_data_structure(resource_datas)
        p.open_list_of_resources(data, commands)


def gather_resources_datas_recursively(card: Card, action: Action, s: SynchronizerABC, resource_datas: dict):
    resource_names = action.get_action_resource_names()
    resources = action.get_action_resource_datas()

    key = (card.name, action.name)
    resource_datas[key] = {'names': [], 'datas': []}
    for name, data in zip(resource_names, resources):
        resource_datas[key]['names'].append(name)
        resource_datas[key]['datas'].append(data)
    if resource_datas[key] == {'names': [], 'datas': []}:  # clean data  (remove if empty)
        del resource_datas[key]

    implementation_card = s.get_implementation_card(action.id)
    for card in s.get_all_descendants(implementation_card):
        for next_action in card.all_actions:
            gather_resources_datas_recursively(card, next_action, s, resource_datas)


def adapter_data_structure(resource_datas: dict) -> tuple:
    cards, actions, names, paths = [], [], [], []
    for (card, action), dict_name_path in resource_datas.items():
        for name, path in zip(dict_name_path['names'], dict_name_path['datas']):
            cards.append(card)
            actions.append(action)
            names.append(name)
            paths.append(path)
    data = cards, actions, names, paths
    return data
