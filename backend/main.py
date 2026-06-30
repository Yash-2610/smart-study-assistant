from fastapi import FastAPI

app = FastAPI(
    title="Smart Study Assistant API",
    description="Backend API for Smart Study Assistant",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Smart Study Assistant Backend is Running!"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }