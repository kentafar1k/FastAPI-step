from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .database import get_db_connection
import sqlite3

app = FastAPI()


class User(BaseModel):
    username: str
    password: str


@app.post("/register")
def register(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Проверяем, существует ли пользователь
        cursor.execute("SELECT username FROM users WHERE username = ?", (user.username,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Username already registered")

        # Создаем нового пользователя
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )

        conn.commit()
        return {"message": "User registered successfully!"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()