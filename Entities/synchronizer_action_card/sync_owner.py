from Entities import Action
from Entities import Card


def sync_owner(policy_action: Action, implementation_card: Card):
    def wrapper(a: Action):
        def wrapped():
            current_owner = None
            for action_in_imple_card in implementation_card.all_actions:
                if not action_in_imple_card.is_done:
                    current_owner = action_in_imple_card.get_owner()
                    break
            a.set_owner(current_owner)
            return a.unwrapped_get_owner()

        return wrapped

    policy_action.unwrapped_get_owner = policy_action.get_owner
    policy_action.get_owner = wrapper(policy_action)
