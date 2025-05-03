from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, RedirectResponse
from .models import User, Feedback

app = FastAPI()

# запуск uvicorn app.main:app --reload --port 1111

class UserOutput(User):
    is_adult: bool = False

feedbacks = []
bad_words = ["залупа", "пенис", "хер"]

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs", status_code=301)

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

@app.post("/feedback")
def get_feedback(feedback: Feedback):
    for word in feedback.message.split():
        if word in bad_words:
            raise ValueError(f"'{word}' - плохое слово")
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

@app.get("/comments")
def get_comments():
    return feedbacks
