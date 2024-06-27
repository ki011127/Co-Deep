import os
from typing import Optional
from fastapi import FastAPI
from models import mongodb
from routers import users, stories, episodes, details, clues, selections

app = FastAPI() # FastAPI 모듈
app.include_router(users.router) # 다른 route파일들을 불러와 포함시킴
app.include_router(stories.router)
app.include_router(episodes.router)
app.include_router(details.router)
app.include_router(clues.router)
app.include_router(selections.router)

@app.on_event("startup")
def on_app_start():
	mongodb.connect()

@app.on_event("shutdown")
async def on_app_shutdown():
	mongodb.close()

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework",
    }