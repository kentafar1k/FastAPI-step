from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from .models import User, Feedback

app = FastAPI()

# запуск uvicorn app.main:app --reload --port 1111

class UserOutput(User):
    is_adult: bool = False

feedbacks = []

@app.get("/")
def read_root():
    return FileResponse("app/public/index.html")

@app.post("/calculate")
def calculate(num1: int = Form(), num2: int = Form()):
    return {"result": num1 + num2}

@app.get("/calculate", response_class=FileResponse)
def calc_form():
    return "app/public/calculate.html"

@app.post("/user", response_model=UserOutput)
def get_user(user: UserOutput = UserOutput(name="andy", age=24)):
    if user.age >= 18:
        user.is_adult = True
    return user

@app.post("/feedback", response_model=Feedback)
def get_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}