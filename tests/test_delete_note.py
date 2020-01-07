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
def mock_delete():
    with patch('pymongo.collection.Collection.find_one_and_delete') as mock_delete:
        yield mock_delete


def test_delete_note(client, mock_delete):
    note_id = '5e13ca9d074eca4a9a9497c6'
    rv = client.delete(f'/notes/{note_id}')
    json_data = rv.get_json()
    mock_delete.assert_called_with({'_id': ObjectId(note_id)})
    assert json_data['data'] is None
