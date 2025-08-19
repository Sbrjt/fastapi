from app.utils import Users, gen_id, hash_pw, verify_password
from tinydb.queries import where


def authenticate_user(email: str, password: str):
    existing_users = Users.search(where('email') == email)

    if not existing_users:
        new_user = {
            'id': gen_id(),
            'email': email,
            'password': hash_pw(password),
        }

        Users.insert(new_user)
        return new_user

    user = existing_users[0]

    if verify_password(password, user['password']):
        return user

    return None
