import fake.explorer as data
from model.explorer import Explorer


def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name) -> Explorer | None:
    return data.get_one(name)


def create(explorer) -> Explorer:
    return data.create(explorer)


def modify(name, explorer) -> Explorer:
    return data.modify(name, explorer)


def replace(name, explorer) -> Explorer:
    return data.replace(name, explorer)


def delete(name) -> bool:
    return data.delete(name)
