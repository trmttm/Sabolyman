from Entities import EntitiesABC
from Gateway import GatewayABC


def execute(file_name:str, e:EntitiesABC, g:GatewayABC):
    data = [['No', 'Name', 'Done', 'Date Created', 'Owner', 'Time Budget', 'Description']]
    for n, action in enumerate(e.active_card.all_actions):
        a = action
        data.append([n, a.name, a.is_done, a.date_created, a.owner, a.time_expected, a.description])
    g.export_data_as_csv(file_name, data)
