from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC):
    s: SynchronizerABC = e.synchronizer
    immediate_parents = s.get_immediate_parents(e.active_card)

    parent_card = immediate_parents[0] if len(immediate_parents) > 0 else None
    if parent_card is not None:
        e.set_filter_parent_card_id(parent_card.id)
        present_card_list.execute(e, p)
