from flask import Blueprint, request

from src.common.utils import response, error_response, validate_body
from src.services.notes import create_note, get_notes, update_note, delete_note

notes = Blueprint('notes', __name__)


@notes.route('/', methods=['POST'])
def create():
    body = request.get_json()
    status, missing_field = validate_body(body, ['title', 'description'])
    if not status:
        return error_response(f'{missing_field} is required')
    try:
        create_note(body)  # _id is automatically added to body
        return response(True, 'Note created successfully', body)
    except Exception as err:
        print(f'::::: Error', err)
        return error_response(str(err))


@notes.route('/', methods=['GET'])
def view():
    conditions = dict(request.args)
    try:
        data = get_notes(conditions)
        return response(True, 'Notes', data)
    except Exception as err:
        print(f'::::: Error', err)
        return error_response(str(err))


@notes.route('/<note_id>', methods=['PUT'])
def update(note_id):
    body = request.get_json()
    try:
        note = update_note(note_id, body)
        return response(True, 'Note updated successfully', note)
    except Exception as err:
        print(f'::::: Error', err)
        return error_response(str(err))


@notes.route('/<note_id>', methods=['DELETE'])
def delete(note_id):
    try:
        delete_note(note_id)
        return response(True, 'Note deleted successfully', None)
    except Exception as err:
        print(f'::::: Error', err)
        return error_response(str(err))
