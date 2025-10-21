#importing fastapi module
from fastapi import FastAPI
from core.config import settings

#creating instance of FastAPI
app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION) 

#now writing first hello FastAPI 

@app.get("/")
def hello():
    return {"msg": "Hello, FastAPI! 🚀"}