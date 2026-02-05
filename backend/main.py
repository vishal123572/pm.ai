from fastapi import FastAPI

app = FastAPI(title="Auto Project Manager AI")

@app.get("/")
def root():
    return {
        "message": "Auto Project Manager AI backend is running",
        "status": "active"
    }
