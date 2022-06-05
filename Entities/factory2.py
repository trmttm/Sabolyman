from .actions import Actions


# Can NOT be depended by Action
def factory_actions(state: dict) -> Actions:
    actions = Actions()
    actions_state = state.get('actions', {})
    actions.load_state(actions_state)
    return actions
