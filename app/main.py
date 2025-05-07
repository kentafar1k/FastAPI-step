from fastapi import FastAPI, Response, Request
from fastapi.responses import FileResponse, RedirectResponse
from .models import User, UserLogin
import jwt
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
            encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
            u["session_token"] = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
            response.set_cookie(key="session_token", value=jwt.decode(encoded_jwt, "secret", algorithms=["HS256"]))
            return {"message": "Normaly", "token": encoded_jwt}
        return {"message": "Wrong credentials"}

@app.get("/user")
async def user(request: Request):
    session_token = request.cookies.get("session_token")
    for u in users:
        if u["session_token"] == session_token and session_token is not None:
            return  user




