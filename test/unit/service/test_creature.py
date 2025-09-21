from model.creature import Creature
from service import creature as code
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


sample = Creature(
    name="Yeti",
    country="CN",
    area="himalayas",
    description="Hirsute himalayan",
    aka="abominable Snowman"
)

def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_asdf_test():
    assert True

def test_get_missing():
    resp = code.get_one("asdf")
    assert  resp is None
