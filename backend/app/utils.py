from os import environ
from uuid import uuid4

import bcrypt
import jwt
from tinydb import TinyDB

from fastapi import HTTPException, Request

JWT_SECRET = environ['JWT_SECRET']

cookie_options = {
    'httponly': True,
    'secure': True,
    'samesite': 'strict',
    'max_age': 30 * 24 * 60 * 60,  # 30 days
}

Users = TinyDB('app/db/user.json')
Notes = TinyDB('app/db/note.json')


def gen_id():
    return str(uuid4())


def sign_jwt(user):
    return jwt.encode(
        user,
        JWT_SECRET,
        algorithm='HS256',
    )


def decode_jwt(req: Request):
    token = req.cookies.get('jwt')

    if not token:
        raise HTTPException(status_code=401, detail='Missing token')

    try:
        user = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=['HS256'],
        )
        req.state.user = user
        return user

    except:
        raise HTTPException(status_code=401, detail='Invalid token')


def hash_pw(password: str):

    hash = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt(),
    )

    return hash.decode()


def verify_password(password: str, hash: str):
    return bcrypt.checkpw(
        password.encode(),
        hash.encode(),
    )
