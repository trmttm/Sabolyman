from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC


def execute(_: EntitiesABC, p: PresentersABC, gateway: GatewayABC, gui_name: str):
    view_model = gateway.load_file_from_package(gui_name, 'Resources')
    p.upon_load_gui(view_model)
