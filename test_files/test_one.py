import pytest

# def test_user_fixture(user_fixture):
#     assert user_fixture.name == "mateusz"

# @pytest.mark.usefixtures('car_fixture')
def test_session(session_fixture):
    pass


class Test:
    @staticmethod
    @pytest.mark.xfail
    def test_car_fixture(car_fixture):
        assert car_fixture.not_customized

    @pytest.mark.xfail
    def test_car_fixture_2(self, car_fixture):
        assert car_fixture.brand == "alfa"
