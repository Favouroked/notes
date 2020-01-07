from unittest.mock import patch

import pytest
from bson.objectid import ObjectId

from src.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_update():
    with patch('pymongo.collection.Collection.find_one_and_update') as mock_update:
        yield mock_update


def test_update_note(client, mock_update):
    note_id = '5e13ca9d074eca4a9a9497c6'
    input_data = {'title': 'Test 1'}
    mock_update.return_value = {'_id': note_id, 'title': 'Test 1'}
    rv = client.put(f'/notes/{note_id}', json=input_data)
    json_data = rv.get_json()
    mock_update.assert_called_with({'_id': ObjectId(note_id)}, {'$set': input_data}, return_document=True)
    assert input_data['title'] == json_data['data']['title']
