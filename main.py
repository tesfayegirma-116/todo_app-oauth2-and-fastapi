from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "status": "200",
        "message": "This is a test API",
        "documentation": "/docs"
    }
