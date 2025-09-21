from model.creature import Creature
import fake.creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name) -> Creature | None:
    return data.get_one(name)


def create(creature) -> Creature:
    return data.create(creature)


def modify(name, creature) -> Creature:
    return data.modify(name, creature)


def replace(name, creature) -> Creature:
    return data.replace(name, creature)


def delete(name) -> bool:
    return data.delete(name)
