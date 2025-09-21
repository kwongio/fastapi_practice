from model.creature import Creature

_creatures = [
    Creature(
        name="Claude Hande",
        country="FR",
        description="보름달이 뜨면 힘름",
        aka="Abmoinaable Snomwman",
        area="Himal"
    ),
    Creature(
        name="Claude Hande",
        country="FR",
        description="보름달이 뜨면 힘름",
        aka="Abmoinaable Snomwman",
        area="Himal"
    )
]

def get_all() -> list[Creature]:
    return _creatures


def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create(creature: Creature) -> Creature:
    return creature


def modify(name: str, creature: Creature) -> Creature:
    return creature


def replace(name: str, creature: Creature) -> Creature:
    return creature


def delete(name: str) -> bool:
    for _creature in _creatures:
        if _creature.name == name:
            return True
    return False
