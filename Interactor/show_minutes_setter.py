import datetime

from Entities import EntitiesABC
from Gateway import GatewayABC
from Presenters import PresentersABC

from . import present_action_list


def execute(e: EntitiesABC, p: PresentersABC, g: GatewayABC, indexes: tuple):
    def upon_ok(time_expected: datetime.timedelta):
        for n, action in enumerate(e.active_card.all_actions):
            if n in indexes:
                action.set_time_expected(time_expected)
        present_action_list.execute(e, p, e.selected_actions_indexes)

    view_model = g.load_file_from_package('minutes_setter.gui', 'Resources')
    p.show_minutes_setter(view_model, upon_ok, **{'title': 'Set Time Expected'})
