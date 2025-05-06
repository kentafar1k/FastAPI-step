from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    name: str
    age: int

class UserLogin(BaseModel):
    login: str
    password: str
    session_token: bool = None