from Entities.action import Action
from Entities.card import Card


def sync_owner(policy_action: Action, implementation_card: Card):
    def wrapper(a: Action):
        def wrapped():
            for action_in_impl_card in implementation_card.all_actions:
                if not action_in_impl_card.is_done:
                    current_owner = action_in_impl_card.get_owner()
                    a.set_owner(current_owner)
                    break
            return a.unwrapped_get_owner()

        return wrapped

    policy_action.unwrapped_get_owner = policy_action.get_owner
    policy_action.get_owner = wrapper(policy_action)
