import os
from bson.objectid import ObjectId
from pymongo import MongoClient

mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost/')
db_name = os.getenv('DB_NAME', 'notes')

client = MongoClient(mongodb_uri)
db = client[db_name]
notes = db['notes']


def create_note(data):
    notes.insert_one(data)


def update_note(note_id, data):
    note = notes.find_one_and_update({'_id': ObjectId(note_id)}, {'$set': data}, return_document=True)
    return note


def delete_note(note_id):
    notes.find_one_and_delete({'_id': ObjectId(note_id)})


def get_notes(conditions):
    if '_id' in conditions:
        conditions['_id'] = ObjectId(conditions['_id'])
    results = notes.find(conditions)
    notes_data = []
    for data in results:
        notes_data.append(dict(data))
    return notes_data
