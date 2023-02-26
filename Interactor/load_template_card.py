from Commands import AddCard
from Entities import EntitiesABC
from Entities.synchronizer_action_card.abc import SynchronizerABC
from Gateway import GatewayABC
from Presenters import PresentersABC
from . import present_card_list


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC, file_name: str):
    card_state = g.load_file(file_name)
    if not card_state.get('is_complex', False):
        command = AddCard(e)
        command.execute()
        card = e.active_card
        card.load_state(card_state)
        e.force_set_ids(card)
        card.update_date_created()
        card.reset_starting_date_to_today()
    else:
        cards_state = card_state.get('cards_state', {})
        sync_state = card_state.get('sync_state').get('sync_state')
        new_cards = {}
        for c_state in cards_state:
            command = AddCard(e)
            command.execute()
            card = e.active_card
            card.load_state(c_state)

            old_id = card.id
            new_cards[old_id] = card
            card.force_set_id()

        s: SynchronizerABC = e.synchronizer
        for card in new_cards.values():
            for a in card.all_actions:
                old_action_id = a.id
                a.force_set_id()

                implementation_card_id = sync_state.get(old_action_id)
                if implementation_card_id in new_cards:
                    implementation_card = new_cards[implementation_card_id]
                    s.synchronize_card_to_action(a, implementation_card)

    present_card_list.execute(e, p)
