from model.explorer import Explorer

_explorers = [
    Explorer(
        name="Claude Hande",
        country="FR",
        description="보름달이 뜨면 힘름"
    ),
    Explorer(
        name="Claude Hande",
        country="FR",
        description="보름달이 뜨면 힘름"
    )
]


def get_all() -> list[Explorer]:
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    return explorer


def replace(name: str, explorer: Explorer) -> Explorer:
    return explorer

def delete(name :  str) -> bool:
    for _explorer in _explorers:
        if _explorer.name == name:
            return True
    return False