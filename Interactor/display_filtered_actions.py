from typing import Callable

from Entities import EntitiesABC


def execute(title: str, filter_action: Callable, feed_back: Callable, e: EntitiesABC):
    text_to_display = ''
    for card in e.all_cards:
        card_text = ''
        for action in card.actions.all_actions:
            if filter_action(action):
                card_text += f'{action.name}\n'
        if card_text != '':
            text_to_display += f'\n\n[{card.name}]\n'
            text_to_display += card_text
    feed_back(title, text_to_display, 400, 600)
