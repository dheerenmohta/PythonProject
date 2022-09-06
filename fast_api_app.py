from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return f"this is profile page of "


@app.get("/profile")
def profile(name:str):
    return f"this is profile page of {name}" # http://127.0.0.1:8000/docs
                                             # http://127.0.0.1:8000/redoc

