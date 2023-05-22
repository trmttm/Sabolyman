import os

from Entities.abc_entities import EntitiesABC
from Entities.card import Card
from Gateway.abc import GatewayABC
from Presenters.abc import PresentersABC

from . import abstract_out
from . import add_new_card
from . import load_template_card
from . import paste_actions_as_alias
from . import show_my_card_information
from . import show_their_card_information


def execute(e: EntitiesABC, g: GatewayABC, p: PresentersABC):
    def callback(file_name):
        initially_selected_card = e.active_card
        if file_name is None:
            pass
        elif file_name == 'default':

            add_new_card.execute(e, p)
            abstract_out_and_insert(initially_selected_card)
        else:
            load_template_card.execute(e, g, p, os.path.join(g.cards_template_path, file_name))
            abstract_out_and_insert(initially_selected_card)

    def abstract_out_and_insert(initially_selected_card: Card):
        # abstract out and paste it to initially selected card
        newly_added_card = e.active_card
        if e.active_card_is_in_my_cards:
            indexes1 = (e.active_card_index,)
            indexes2 = ()
        else:
            indexes1 = ()
            indexes2 = (e.active_card_index,)
        abstract_out.execute(e, indexes1, indexes2, )
        e.set_active_card(initially_selected_card)
        paste_actions_as_alias.execute(e, p)
        # focus on new card
        e.set_active_card(newly_added_card)
        if initially_selected_card in e.my_visible_cards:
            show_my_card_information.execute(e, p, (e.active_card_index,))
        else:
            show_their_card_information.execute(e, p, (e.active_card_index,))
        e.set_show_this_card(newly_added_card)

    file_names = g.get_files_in_the_folder(g.cards_template_path)
    display = ('Default',) + tuple(f.split('.')[0] for f in file_names if f[0] != '.')
    data = ('default',) + tuple(f for f in file_names if f[0] != '.')

    p.ask_user_to_select_from_a_list(dict(zip(display, data)), callback)
