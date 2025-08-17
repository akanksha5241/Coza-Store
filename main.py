# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.auth import router as auth_router
from app.database import create_user_table, create_contacts_table
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)

@app.on_event("startup")
def on_startup():
    create_user_table()
    create_contacts_table()
