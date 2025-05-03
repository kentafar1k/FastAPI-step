from pydantic import BaseModel, constr


class User(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: constr(min_length=2, max_length=50)
    message: constr(min_length=10, max_length=500)