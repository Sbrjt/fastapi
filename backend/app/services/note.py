from app.utils import Notes, gen_id
from tinydb import where


def get_notes(userid):

    notes = Notes.search(
        where('userid') == userid,
    )

    return notes


def add_note(note, userid):

    new_note = {
        'id': gen_id(),
        'userid': userid,
        **dict(note),
    }

    Notes.insert(new_note)
