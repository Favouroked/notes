import pytest

from src.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert 'Welcome' in json_data['message']
