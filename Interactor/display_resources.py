import Utilities
from Entities import Action
from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Gateway.abc import GatewayABC
from Presenters import PresentersABC

from convert_uri_to_folder_path import open_folder


def execute(e: EntitiesABC, p: PresentersABC, g: GatewayABC):
    s: SynchronizerABC = e.synchronizer
    action = e.active_action
    commands = {'open_file': lambda uri: Utilities.open_file, 'open_folder': lambda uri: open_folder(g, uri)}
    if action is not None:
        resource_datas = {}
        gather_resources_datas_recursively(action, s, resource_datas)
        p.open_list_of_resources(resource_datas, commands)


def gather_resources_datas_recursively(action: Action, s: SynchronizerABC, resource_datas: dict):
    action_id = action.id
    resource_names = action.get_action_resource_names()
    resources = action.get_action_resource_datas()

    resource_datas[action_id] = {'names': [], 'datas': []}
    for name, data in zip(resource_names, resources):
        resource_datas[action_id]['names'].append(name)
        resource_datas[action_id]['datas'].append(data)
    if resource_datas[action_id] == {'names': [], 'datas': []}:  # clean data  (remove if empty)
        del resource_datas[action_id]

    implementation_card = s.get_implementation_card(action_id)
    for card in s.get_all_descendants(implementation_card):
        for next_action in card.all_actions:
            gather_resources_datas_recursively(next_action, s, resource_datas)
