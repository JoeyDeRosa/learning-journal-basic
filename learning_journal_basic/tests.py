import pytest
from pyramid import testing


@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns data."""
    from .views import list_page
    response = list_page(req)
    assert '<title>list page</title>' in response
