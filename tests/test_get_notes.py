from unittest.mock import patch

import pytest

from src.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_find():
    with patch('pymongo.collection.Collection.find') as mock_find:
        yield mock_find


def test_notes_view_with_no_conditions(client, mock_find):
    mock_find.return_value = [{'title': 'Test'}, {'title': 'Test 1'}]
    rv = client.get('/notes/')
    json_data = rv.get_json()
    mock_find.assert_called_with({})
    assert len(json_data['data']) == 2


def test_notes_view_with_conditions(client, mock_find):
    mock_find.return_value = [{'title': 'Test'}]
    rv = client.get('/notes/?title=Test')
    json_data = rv.get_json()
    mock_find.assert_called_with({'title': 'Test'})
    assert 'Test' == json_data['data'][0]['title']
    assert len(json_data['data']) == 1
