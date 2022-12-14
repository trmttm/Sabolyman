from typing import Callable

from Entities import EntitiesABC


def execute(title: str, filter_action: Callable, feed_back: Callable, e: EntitiesABC, text_color: str = 'black'):
    text_to_display = ''
    counter_card = 0
    counter_all_actions = 0
    for card in e.all_cards:
        card_text = ''
        counter_action = 0
        for action in card.actions.all_actions:
            if filter_action(action):
                card_text += f'\t{counter_action + 1}\t{action.name}\n'
                counter_action += 1
                counter_all_actions += 1

        if card_text != '':
            if counter_card > 0:
                text_to_display += '\n\n'
            text_to_display += f'【{counter_card + 1} {card.name}】\n'
            counter_card += 1

            text_to_display += card_text

    prefix = f'Total {counter_card} cards, {counter_all_actions} actions\n\n'
    kwargs = {'by_textbox': True, 'text_color': text_color}
    feed_back(title, prefix + text_to_display, 800, 800, **kwargs)
