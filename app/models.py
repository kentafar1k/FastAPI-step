from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: constr(min_length=2, max_length=50)
    message: constr(min_length=10, max_length=500)


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    is_subscribed: bool