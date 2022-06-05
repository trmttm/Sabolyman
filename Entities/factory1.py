from .files import Files
from .person import Person


# Can be depended by any Entities
def factory_files(state: dict) -> Files:
    files = Files()
    flies_state = state.get('files', {})
    files.load_state(flies_state)
    return files


def factory_person(state: dict, key: str) -> Person:
    person = Person('')
    owner_state = state.get(key, {})
    person.load_state(owner_state)
    return person
