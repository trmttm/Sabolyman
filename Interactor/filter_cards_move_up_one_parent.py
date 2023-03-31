from Entities.abc_entities import EntitiesABC
from Entities.card import Card
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Interactor import present_card_list
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC):
    s: SynchronizerABC = e.synchronizer
    immediate_parents = s.get_immediate_parents(e.active_card)

    if len(immediate_parents) == 0:
        parent_card = None
    elif len(immediate_parents) == 1:
        parent_card = immediate_parents[0]
    else:
        parent_card = None

        def callback(card_id: str):
            for candidate in immediate_parents:
                if candidate.id == card_id:
                    apply_filter_and_display(e, p, candidate)

        parent_name_to_id = dict(zip(tuple(c.name for c in immediate_parents), tuple(c.id for c in immediate_parents)))
        p.ask_user_to_select_from_a_list(parent_name_to_id, callback)

    apply_filter_and_display(e, p, parent_card)


def apply_filter_and_display(e: EntitiesABC, p: PresentersABC, parent_card: Card):
    if parent_card is not None:
        e.set_filter_parent_card_id(parent_card.id)
        present_card_list.execute(e, p)
