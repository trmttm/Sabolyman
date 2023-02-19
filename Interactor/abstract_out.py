from Commands import CreateAction
from Entities import EntitiesABC


def execute(e: EntitiesABC):
    implementation_card = e.active_card

    command = CreateAction(e)
    action_policy = command.execute()

    e.synchronize_action_to_card(action_policy, implementation_card)
    e.copy_actions((action_policy,))
    print(f'Implementation card {implementation_card.name} is copied.')
