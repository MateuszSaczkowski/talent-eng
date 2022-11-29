import pytest

from src.applications.GitubUI import GitHubUI
from src.applications.GitHubApi import GitHubApi
from src.models.car import Car
from src.models.user import User


@pytest.fixture(scope="session")
def session_fixture():
    print("---start of test---")

    yield

    print("--end of test---")


@pytest.fixture()
def user_fixture():
    user = User("mateusz", "mati@EE.com")
    user.create_user_in_db()

    yield user

    user.remove_user_in_db()


@pytest.fixture(scope="class")
def car_fixture():
    alfa = Car("alfa", "brera", True)
    alfa.add_car_to_db()

    yield alfa

    alfa.del_car_from_db()


@pytest.fixture()
def api_username_log():
    api_username = GitHubApi()
    if api_username.login("user") is False:
        raise Exception("user\s login failed")

    yield api_username


@pytest.fixture()
def github_ui_app():
    github_ui_app = GitHubUI()
    github_ui_app.open_base_page()

    yield github_ui_app
