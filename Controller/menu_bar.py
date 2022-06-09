import datetime

from interface_view import ViewABC

from Entities import EntitiesABC
from Interactor import InteractorABC


def configure_menu_bar(v: ViewABC, i: InteractorABC, e: EntitiesABC):
    menu_bar_model = {
        'Cards': {
            'Duplicate': lambda: i.duplicate_selected_card()
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
    now = datetime.datetime.now()
    month = f'0{now.month}' if now.month < 10 else f'{now.month}'
    day = f'0{now.day}' if now.day < 10 else f'{now.day}'
    hour = f'0{now.hour}' if now.hour < 10 else f'{now.hour}'
    minute = f'0{now.minute}' if now.minute < 10 else f'{now.minute}'
    return f'{now.year}{month}{day}_{hour}{minute}'
