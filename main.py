import uvicorn
import os
from fastapi import FastAPI
from app.routes import tutor
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Swedish-Arabic Tutor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tutor.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Swedish-Arabic Tutor API"}
