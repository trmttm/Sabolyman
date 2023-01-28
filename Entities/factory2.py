from .actions import Actions


# Can NOT be depended by Action
def factory_actions(state: dict, alias_actions_dictionary: dict = None) -> Actions:
    if alias_actions_dictionary is None:
        alias_actions_dictionary = {}
    actions = Actions()
    actions_state = state.get('actions', {})
    actions.load_state(actions_state, alias_actions_dictionary)
    return actions
