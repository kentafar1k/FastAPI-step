from urllib import request

from fastapi import FastAPI, Response, Request
from fastapi.responses import FileResponse, RedirectResponse
from .models import User, UserLogin
import random

app = FastAPI()

# запуск uvicorn app.main:app --reload --port 1111
users = [
    {
        "login": "andy",
        "password": "1234",
        "session_token": None
    },
    {
        "login": "dandy",
        "password": "2222",
        "session_token": None
    }
]


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs", status_code=301)

@app.post("/login")
async def login(user: UserLogin, response: Response):
    for u in users:
        if u["login"] == user.login and u["password"] == user.password:
            token = str(random.randint(100, 999))
            u["session_token"] = token
            response.set_cookie(key="session_token", value=token)
            return {"message": "Normaly"}
        return {"message": "Wrong credentials"}

@app.get("/user")
async def user(request: Request):
    session_token = request.cookies.get("session_token")
    for u in users:
        if u["session_token"] == session_token and session_token is not None:
            return  {"session_token": session_token}




