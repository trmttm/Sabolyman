import os

from Utilities import datetime_to_str

from Entities import EntitiesABC
from Entities.action import Action
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Gateway import GatewayABC


def execute(e: EntitiesABC, g: GatewayABC):
    file_name = os.path.join(g.gantt_chart_folder_path, 'gantt chart data.csv')
    data = create_data(e)
    g.export_data_as_csv(file_name, data)


def create_data(e: EntitiesABC):
    data = [['No', 'Name', 'Done', 'Date Created', 'Owner', 'Start From', 'Dead Line', 'Time Budget', 'Description']]
    level = -1
    index_n = ''
    separator = '.'
    kw = {
        'data': data,
        'level': level,
        'index_n': index_n,
        'separator': separator,
    }
    add_data_recursively(e.active_card.all_actions, e, **kw)
    return data


def add_data_recursively(actions: list[Action, ...], e: EntitiesABC, **kwargs):
    s: SynchronizerABC = e.synchronizer
    data = kwargs.get('data')
    level = kwargs.get('level')
    index_n = kwargs.get('index_n')
    separator = kwargs.get('separator')

    level += 1

    for n, action in enumerate(actions):
        index_n = identify_next_index(index_n, level, n, separator)
        insert_data(action, data, index_n)
        if s.action_has_implementation_card(action.id):
            recursively_add_data(e, s, action, data, index_n, level, separator)


def recursively_add_data(e, s, action, data, index_n, level, separator):
    kw = {
        'data': data,
        'level': level,
        'index_n': index_n,
        'separator': separator,
    }
    implementation_card = s.get_implementation_card(action.id)
    add_data_recursively(implementation_card.all_actions, e, **kw)


def identify_next_index(index_n: str, level: int, n: int, separator: str):
    lower_level_index = n + 1  # starts from 0 vs 1
    if level == 0:
        index_n = str(lower_level_index)
    elif lower_level_index == 1:
        index_n = f'{index_n}{separator}{lower_level_index}'
    else:
        index_n = str(separator.join(index_n.split(separator)[:-1]) + f'.{lower_level_index}')
    return index_n


def insert_data(action: Action, data: list, index_n: str):
    data.append([index_n,
                 action.name,
                 action.is_done,
                 datetime_to_str(action.date_created),
                 action.get_owner(),
                 datetime_to_str(action.get_start_from()),
                 datetime_to_str(action.get_dead_line()),
                 action.time_expected,
                 action.description,
                 ])
