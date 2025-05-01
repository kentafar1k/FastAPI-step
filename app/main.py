from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

# запуск uvicorn app.main:app --reload --port 1111

@app.get("/")
def read_root():
    return FileResponse("app/public/index.html")

@app.post("/calculate")
def calculate(num1: int = Form(), num2: int = Form()):
    return {"result": num1 + num2}

@app.get("/calculate", response_class=FileResponse)
def calc_form():
    return "app/public/calculate.html"