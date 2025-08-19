from pydantic import BaseModel


class New_Note(BaseModel):
    title: str
    content: str


class UserInput(BaseModel):
    email: str
    password: str
