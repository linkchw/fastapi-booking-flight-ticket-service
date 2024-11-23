from apis.base import api_router
from core.config import setting
from db.base import Base
from db.session import engine
from fastapi import FastAPI


def include_router(app):
    app.include_router(api_router)


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=setting.PROJECT_NAME, version=setting.PROJECT_VERSION)
    create_table()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"msg": "Welcome to Flight Ticket Service"}
