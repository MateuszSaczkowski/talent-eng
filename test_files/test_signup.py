import pytest


@pytest.mark.xfail
def test_api_username(api_username_log):
    body = api_username_log.research_repo("TE_2.0")
    assert body
