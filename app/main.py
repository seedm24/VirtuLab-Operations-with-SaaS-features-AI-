from fastapi import FastAPI
from app import other_modules  # Adjust based on your actual module names

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to VirtuLab Operations!"}
