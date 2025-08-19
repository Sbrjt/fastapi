from app.schema import New_Note
from app.services.note import add_note, get_notes
from app.utils import decode_jwt

from fastapi import APIRouter, Depends, Request

router = APIRouter(dependencies=[Depends(decode_jwt)])


@router.get("/all")
def get_notes_route(req: Request):

    userid = req.state.user['id']

    return get_notes(userid)


@router.post("/add")
def add_note_route(note: New_Note, req: Request):

    userid = req.state.user['id']

    add_note(note, userid)

    return {"message": "New Note added 🥳"}
