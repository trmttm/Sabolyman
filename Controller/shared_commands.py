from interface_view import ViewABC

import WidgetNames as wn
from Interactor import InteractorABC


def paste_resources_then_display_resources(i: InteractorABC, app: ViewABC):
    i.paste_resources()
    i.feed_back_user_by_popup('Success', 'Resources pasted.')
    app.select_note_book_tab(wn.notebook_actions, 2)


def paste_description_then_display_notex(i: InteractorABC, app: ViewABC):
    i.paste_description()
    i.feed_back_user_by_popup('Success', 'Description pasted.')
    app.select_note_book_tab(wn.notebook_actions, 1)
