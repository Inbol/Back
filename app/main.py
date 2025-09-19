from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routers import users, enterprises, predict, login# Importación de las rutas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Lista de orígenes permitidos
origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(users.router)
app.include_router(enterprises.router)
app.include_router(predict.router)
app.include_router(login.router)