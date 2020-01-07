from unittest.mock import patch

import pytest

from src.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_insert():
    with patch('pymongo.collection.Collection.insert_one') as mock_insert:
        yield mock_insert


def test_insert_note_with_incomplete_fields(client):
    rv = client.post('/notes/', json={'title': 'Test'})
    json_data = rv.get_json()
    assert 'description is required' == json_data['message']


def test_insert_note(client, mock_insert):
    note_data = {'title': 'Test', 'description': 'Test Description'}
    rv = client.post('/notes/', json=note_data)
    json_data = rv.get_json()
    mock_insert.assert_called_with(note_data)
    assert 'Test' == json_data['data']['title']
