import pytest

from src.mypkg.app import MyObject


@pytest.fixture
def app_fixture() -> MyObject:
    return MyObject(5.0, 5.0, 5.0)


def test_area(app_fixture: MyObject) -> None:
    assert app_fixture.calculate_area() == 25


def test_volume(app_fixture: MyObject) -> None:
    assert app_fixture.calculate_volume() == 125
