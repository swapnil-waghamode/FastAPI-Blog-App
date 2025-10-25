#importing fastapi module
from fastapi import FastAPI
from core.config import settings

from db.session import engine
from db.base_class import Base


def db_table():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    db_table()
    return app

app = start_application()
 

#now writing first hello FastAPI 

@app.get("/")
def hello():
    return {"msg": "Hello, FastAPI! 🚀"}
