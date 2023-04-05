import pytest

from src.mypkg.app import App


@pytest.fixture
def app_fixture() -> App:
    return App()


def test_area(app_fixture: App) -> None:
    assert app_fixture.calculate_area(5.0, 5.0) == 25


def test_volume(app_fixture: App) -> None:
    assert app_fixture.calculate_volume(5.0, 5.0, 5.0) == 125
