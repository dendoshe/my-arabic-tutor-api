from fastapi import FastAPI
from app.routes import tutor

app = FastAPI(title="Swedish-Arabic Tutor API")

app.include_router(tutor.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Swedish-Arabic Tutor API"}
