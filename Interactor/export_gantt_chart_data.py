import os

from Entities import EntitiesABC
from Gateway import GatewayABC


def execute(e: EntitiesABC, g: GatewayABC):
    file_name = os.path.join(g.gantt_chart_folder_path, 'gantt chart data.csv')
    data = [['No', 'Name', 'Done', 'Date Created', 'Owner', 'Start From', 'Dead Line', 'Time Budget', 'Description']]
    for n, action in enumerate(e.active_card.all_actions):
        a = action
        data.append([n,
                     a.name,
                     a.is_done,
                     a.date_created,
                     a.get_owner(),
                     a.get_start_from(),
                     a.get_dead_line(),
                     a.time_expected,
                     a.description,
                     ])
    g.export_data_as_csv(file_name, data)
