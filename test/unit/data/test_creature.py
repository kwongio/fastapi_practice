import pytest

from error import Duplicate
from model.creature import Creature

@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Yeti",
        country="CN",
        area="himalayas",
        description="Hirsute himalayan",
        aka="abominable Snowman"
    )

