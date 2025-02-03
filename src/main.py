from fastapi import FastAPI
import os

app = FastAPI()
NAME = os.getenv("NAME", "Anonymous")

@app.get("/me")
async def get_me():
    return {"message": f"Hello, my name is {NAME}"}