from fastapi import FastAPI
import os

environment = os.getenv("APP_ENV", "development")

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "failed"}

@app.get("/info")
def info():
    return {"name": "devops-learning","version": "0.1.0","environment": environment}