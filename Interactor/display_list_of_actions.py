import datetime
from typing import Callable

import Utilities
from Entities import EntitiesABC
from Presenters import PresentersABC


def execute(e: EntitiesABC, p: PresentersABC, owner_name: str, from_: datetime.datetime,
            to_: datetime.datetime, sort_cards: Callable):
    def callback(state: tuple):
        number_of_changes = 1
        for each_action_state in state:
            action_id, due_date_str, is_done, owner = each_action_state
            action = e.get_action_by_id(action_id)
            new_dead_line = Utilities.str_to_date_time(due_date_str)

            initial_dead_line = action.get_dead_line()
            i, n = initial_dead_line, new_dead_line
            if datetime.datetime(i.year, i.month, i.day,i.hour,i.minute) != datetime.datetime(n.year, n.month, n.day, n.hour,n.minute):
                action.set_dead_line(new_dead_line)
                print(f'{number_of_changes} New deadline [{action.name}]. {initial_dead_line} -> {new_dead_line}')
                number_of_changes += 1
            if action.is_done != is_done:
                if is_done:
                    action.mark_done()
                    print(f'{number_of_changes} [{action.name}] is marked Done.')
                else:
                    action.mark_not_done()
                    print(f'{number_of_changes} [{action.name}] is marked Not Done.')
                number_of_changes += 1
            if action.get_owner().name != owner:
                action.set_owner(e.create_new_person(owner))
                print(f'{number_of_changes} [{action.name}] has new owner {action.get_owner()}.')
                number_of_changes += 1
        if number_of_changes > 1:
            sort_cards()

    data = create_data_for_action_list(e, owner_name, from_, to_)
    p.open_display_list_of_actions(data, callback)


def create_data_for_action_list(e: EntitiesABC, owner_name: str, from_: datetime.datetime,
                                to_: datetime.datetime) -> dict:
    from Entities.synchronizer_action_card.abc import SynchronizerABC
    import GUI.list_of_actions as c

    s: SynchronizerABC = e.synchronizer
    filter_by_owner = owner_name.strip() != ''
    data = {
        c.KEY_DATE: to_,
    }
    card_states = []
    for card in e.all_cards:
        if not card.is_done:
            card_state = {
                c.CARD_NAME: card.name,
                c.KEY_ACTION_IDS: [],
                c.KEY_NAMES: [],
                c.KEY_DONE_OR_NOT: [],
                c.KEY_DUE_DATES: [],
                c.KEY_OWNERS: [],
            }
            for action in card.all_actions:
                has_no_implementation = (not s.action_has_implementation_card(action.id))
                not_done = (not action.is_done)
                due_date_within_specified_range = from_ <= action.get_dead_line() <= to_
                owner_matches = (not filter_by_owner) or (action.get_owner().name == owner_name)
                if has_no_implementation and not_done and due_date_within_specified_range and owner_matches:
                    card_state[c.KEY_ACTION_IDS].append(action.id)
                    card_state[c.KEY_NAMES].append(action.name)
                    card_state[c.KEY_DONE_OR_NOT].append(action.is_done)
                    card_state[c.KEY_DUE_DATES].append(action.get_dead_line())
                    card_state[c.KEY_OWNERS].append(action.get_owner())
            if len(card_state[c.KEY_NAMES]) > 0:
                card_state[c.KEY_ACTION_IDS] = tuple(card_state[c.KEY_ACTION_IDS])
                card_state[c.KEY_NAMES] = tuple(card_state[c.KEY_NAMES])
                card_state[c.KEY_DONE_OR_NOT] = tuple(card_state[c.KEY_DONE_OR_NOT])
                card_state[c.KEY_DUE_DATES] = tuple(card_state[c.KEY_DUE_DATES])
                card_state[c.KEY_OWNERS] = tuple(card_state[c.KEY_OWNERS])
                card_states.append(card_state)
    card_states = tuple(card_states)
    data.update({c.KEY_CARD_STATES: card_states})
    return data
