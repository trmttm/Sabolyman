import datetime

import Utilities
from interface_view import ViewABC

from Entities import EntitiesABC
from Interactor import InteractorABC
from . import state


def configure_menu_bar(v: ViewABC, i: InteractorABC, e: EntitiesABC):
    menu_bar_model = {
        'Cards': {
            'Duplicate Card [cmd+d]': lambda: i.duplicate_selected_card(),
            'Set Color [cmd+c]': lambda: i.set_color_to_cards(
                state.get_my_cards_selected_indexes(v),
                state.get_their_cards_selected_indexes(v),
                v.ask_color()),
        },
        'File': {
            'Save Sate': lambda: i.save_to_file(v.select_save_file(initialfile=default_file_name(e))),
            'Load State': lambda: i.load_state_from_file(v.select_open_file()),
            'Save as Template Card': lambda: i.save_as_template_card(v.select_save_file()),
            'Add Template Card': lambda: i.add_template_card(v.select_open_file()),
        },
    }
    v.update_menu_bar(menu_bar_model)


def default_file_name(e: EntitiesABC) -> str:
    return f'{now()}_{e.user.name.replace(" ", "_")}.sb'


def now() -> str:
    f = Utilities.get_two_digit_str_from_int
    now = datetime.datetime.now()
    month = f(now.month)
    day = f(now.day)
    hour = f(now.hour)
    minute = f(now.minute)
    return f'{now.year}{month}{day}_{hour}{minute}'
