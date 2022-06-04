from interface_view import ViewABC

from Interactor import InteractorABC
from . import state as s


def configure_controller(v: ViewABC, i: InteractorABC):
    name = 'my_balls'
    f = v.bind_command_to_widget

    f(f'btn_{name}_add', lambda: i.add_new_card())
    f(f'btn_{name}_delete', lambda: i.delete_selected_cards(s.get_my_balls_selected_indexes(v)))
    f('tree_my_balls', lambda: i.show_card_information(s.get_my_balls_selected_indexes(v)))
    f('entry_name', lambda *_: i.set_card_name(s.get_card_name(v)))
    f('entry_dead_line', lambda *_: i.set_dead_line(s.get_dead_line_str(v)))
