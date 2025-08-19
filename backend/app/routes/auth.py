from app.schema import UserInput
from app.services.auth import authenticate_user
from app.utils import cookie_options, decode_jwt, sign_jwt

from fastapi import APIRouter, Depends, HTTPException, Response

router = APIRouter()


@router.post("/login")
def login_route(res: Response, cred: UserInput):

    user = authenticate_user(cred.email, cred.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = sign_jwt(
        {
            'id': user['id'],
            'email': user['email'],
        }
    )

    res.set_cookie(
        key='jwt',
        value=token,
        **cookie_options,
    )

    print('Logged in: ', cred.email)
    return user


@router.get("/logout")
def logout_route(res: Response):
    res.delete_cookie(key='jwt')
    return {"message": "Logged out"}


@router.get("/me")
def me_route(user=Depends(decode_jwt)):
    return user
