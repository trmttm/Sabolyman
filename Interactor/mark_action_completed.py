from Entities import EntitiesABC
from Presenters import PresentersABC
from . import present_action_list
from . import present_card_list
from . import set_action_complete_time
from . import set_action_is_done_or_not


def execute(e: EntitiesABC, p: PresentersABC, done_or_not: bool):
    set_action_complete_time.execute(e, done_or_not)
    set_action_is_done_or_not.execute(e, p, done_or_not)
    present_action_list.execute(e, p)
    present_card_list.execute(e, p)
